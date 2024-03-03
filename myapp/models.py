from django.db import models

# Create your models here.
class ImagePost(models.Model):
  title = models.CharField(max_length=100)
  imageURL = models.TextField()
  def __str__(self):
    return self.title