from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.blog import Blog
from ..serializers import BlogSerializer

# Create your views here.
class Blog(generics.ListCreateAPIView):
    def get(self, request):
        """Index request"""
        blog = Blog.objects.all()
        #blog = Blog.objects.filter(owner = request.user.id)
        data = BlogSerializer(blog, many=True).data
        return Response(data)

    # Serializer classes are required for endpoints that create data
    serializer_class = BlogSerializer

    def post(self, request):
      """Create request"""
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
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        blog = get_object_or_404(Blog, pk=pk)
        # Validate updates with serializer
        bs = BlogSerializer(blog, data=request.data['blog'])
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        return Response(bs.errors, status=status.HTTP_400_BAD_REQUEST)
