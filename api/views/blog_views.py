from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.blogs import Blog
from ..serializers import BlogSerializer, UserSerializer

# Create your views here.
# All the views in `Blogs` will require tokens & use TokenAuthentication
class Blog(generics.ListCreateAPIView):
  permission_classes =()
  serializer_class = BlogSerializer
  def get(self, request):
      """Index request"""
      # Using the django `.filter` method & passing it "named argument"
      # The name is the field (owner), the value is the currently
      # signed in user's ID
      blogs = Blog.objects.all()#filter(owner=request.user.id)
      data = BlogSerializer(blogs, many=True).data
      return Response({ 'blogs': data })

  def post(self, request):
    """Create request"""
    # Add user to request object
    request.data['blog']['owner'] = request.user.id
    # Pass the request data to the serializer to validate it
    blog = BlogSerializer(data=request.data['blog'])
    if blog.is_valid():
      blog.save()
      return Response({ 'blog': blog.data }, status=status.HTTP_201_CREATED)
    else:
      return Response(blog.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the blog to show
        blog = get_object_or_404(Blog, pk=pk)

        # Only want to show owned blogs?
        if not request.user.id == blog.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this blog')

        # Run the data through the serializer so it's formatted
        data = BlogSerializer(blog).data

        return Response({ 'blog': data })


    def delete(self, request, pk):
        """Delete request"""
        # Locate blog to delete
        blog = get_object_or_404(Blog, pk=pk)
        if not blog.owner.id == request.user.id:
            raise PermissionDenied('You do not own this blog.')
        # Only delete if the user owns the  blog
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['blog'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['blog'].get('owner', False):
            del request.data['blog']['owner']
        # Locate Blog
        # get_object_or_404 returns a object representation of our Blog
        blog = get_object_or_404(Blog, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == blog.owner.id:
            raise PermissionDenied('You do not own this Blog')

        # Add owner to data object now that we know this user owns the resource
        request.data['blog']['owner'] = request.user.id

        # Validate updates with serializer
        data = BlogSerializer(blog, data=request.data['blog'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
