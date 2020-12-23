from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models.blog import Blog

from django.conf import settings

class BlogSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'blogtitle', 'description', 'date', 'author', 'blogtext')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_blog(**validated_data)

class BlogRegisterSerializer(serializers.Serializer):
    blogtitle = serializers.CharField(max_length=500)
    desrciption = models.CharField(max_length=500)
    date = models.DateField('Date', auto_now_add=True)
    author = models.CharField(max_length=100)
    blogtext = models.CharField(max_length=1000)

    def validate(self, data):
        # Ensure blogtitle & description exist
        if not data['blogtitle'] or not data['description']:
            raise serializers.ValidationError('Please include a title and subject.')


        if data['blogtitle'] != data['blogtitle']:
            raise serializers.ValidationError('Please include a title.')
        # if all is well, return the data
        return data

class UpdateBlogSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
