from django.urls import path
from .views.blog_views import BlogCreate, BlogIndex, BlogDelete, BlogShow, BlogUpdate, Blog, BlogDetail


urlpatterns = [
  	# Restful routing
    path('blog/', Blog.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('index/', BlogIndex.as_view(), name='index'),
    path('delete/', BlogDelete.as_view(), name='delete'),
    path('show/', BlogShow.as_view(), name='show'),
    path('update/', BlogUpdate.as_view(), name='update'),
]
