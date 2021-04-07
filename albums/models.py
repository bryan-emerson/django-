from django.db import models

# Create your models here.

#artist model
class Artist(models.Model):
  # Artist model fields
  name = models.CharField(max_length=120)
  bio = models.TextField()

  #string magic method
  #makes debugging easier
  def __str__(self):
    return self.name

#album model
class Album(models.Model):
  #album fields
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
  year = models.IntegerField()
  title = models.CharField(max_length=120)

  def __str__(self):
    return self.title