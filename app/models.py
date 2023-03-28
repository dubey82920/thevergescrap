from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=32, unique=True)
    url = models.URLField(null=True)
    headline = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=20,null=True)
    