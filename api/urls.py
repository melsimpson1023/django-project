from django.urls import path
from .views.blog_views import Blogs, BlogDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword


urlpatterns = [
  	# Restful routing
    path('blog/', Blogs.as_view(), name='blogs'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
]
