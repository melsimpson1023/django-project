from django.db import models

# Create your models here.
class Blog(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  blogtitle = models.CharField(max_length=500)
  desrciption = models.CharField(max_length=500)
  date = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  blogtext = models.CharField(max_length=1000)

  def __str__(self):
    # This must return a string
    return f"The blog named '{self.blogtitle}' is {self.description} in blog. This is the date {self.date} , Author {self.author}, BlogText {self.blogtext}"

  def as_dict(self):
    """Returns dictionary version of Blog models"""
    return {
        'id': self.id,
        'blogtitle': self.blogtitle,
        'description': self.description,
        'date': self.date,
        'author': self.author,
        'blogtext': self.blogtext
    }
