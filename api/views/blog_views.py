from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
#from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.blog import Blog
from ..serializers import BlogSerializer#, UserSerializer

# Create your views here.
# All the views in `Blogs` will require tokens & use TokenAuthentication
class Blog(generics.ListCreateAPIView):
  # permission_classes = []
  def get(self, request):
      """Index request"""
      blogs = Blog.objects.all()
      # Using the django `.filter` method & passing it "named argument"
      # The name is the field (owner), the value is the currently
      # signed in user's ID
      #blogs = Blog.objects.filter(owner=request.user.id)
      data = BlogSerializer(blogs, many=True).data
      return Response(data)

  serializer_class = BlogSerializer
  def post(self, request):
    """Create request"""
    # Add user to request object
    request.data['blog']['owner'] = request.user.id
    # Pass the request data to the serializer to validate it
    blog = BlogSerializer(data=request.data['blog'])
    if blog.is_valid():
      blog.save()
      return Response(blog.data, status=status.HTTP_201_CREATED)
    else:
      return Response(blog.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        """Show request"""
        blog = get_object_or_404(Blog, pk=pk)
        data = BlogSerializer(blog).data

        # `data` should be a dictionary of our Blog instance
        print(data, request.user.id)
        # Compare `data['owner']` against `request.user.id`
        # If they're the same, we can show the Mango
        # If they don't match, throw a permissions error
        if not data['owner'] == request.user.id:
            raise PermissionDenied('You dont own this Blog!')

        return Response(data)


    def delete(self, request, pk):
        """Delete request"""
        blog = get_object_or_404(Blog, pk=pk)
        if not blog.owner.id == request.user.id:
            raise PermissionDenied('You do not own this blog.')
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        blog = get_object_or_404(Blog, pk=pk)
        # `blog` is an object (not a dictionary) so we dot onto the `owner` and `id` and compare that against `request.user.id`
        if not blog.owner.id == request.user.id:
            raise PermissionDenied('You do not own this Blog')

        # Before serializing data and after confirming ownership
        # We attach the currently signed in user as the owner
        request.data['blog']['owner'] = request.user.id

        # Validate updates with serializer
        bs = BlogSerializer(blog, data=request.data['blog'])

        # We cannot access `bs.data` (our serialized data) before calling is_valid()
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        return Response(bs.errors, status=status.HTTP_400_BAD_REQUEST)
