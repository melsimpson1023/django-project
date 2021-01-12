from django.db import models
# importing the get_user_model method which will locate the model that our project is using as 'User'
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=500)
  subject = models.CharField(max_length=500)
  date = models.DateField('Date', auto_now_add=True)
  text = models.CharField(max_length=1000)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  def __str__(self):
    # This must return a string
    return f"The blog named '{self.title}'."
    #return self.name

  def as_dict(self):
    """Returns dictionary version of Blog models"""
    return {
        'id': self.id,
        'title': self.title,
        'subject': self.subject,
        'date': self.date,
        'text': self.text
    }
