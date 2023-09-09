from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    comment=models.TextField()

# Create your models here.