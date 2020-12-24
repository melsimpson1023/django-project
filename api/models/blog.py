from django.db import models
# importing the get_user_model method which will locate the model that our project is using as 'User'
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  blogtitle = models.CharField(max_length=500)
  blogsubject = models.CharField(max_length=500)
  date = models.DateField('Date', auto_now_add=True)
  author = models.CharField(max_length=100)
  blogtext = models.CharField(max_length=1000)

  # 'owner' will be a foreignkey pointing to the 'user'model which we'll access with the get_user_model
  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
  )


  def __str__(self):
    # This must return a string
    return f"The blog named '{self.blogtitle}' this is subject {self.blogsubject} in blog. This is the date {self.date} , Author {self.author}, BlogText {self.blogtext}"
    #return self.name

  def as_dict(self):
    """Returns dictionary version of Blog models"""
    return {
        'id': self.id,
        'blogtitle': self.blogtitle,
        'blogsubject': self.blogsubject,
        'date': self.date,
        'author': self.author,
        'blogtext': self.blogtext
    }
