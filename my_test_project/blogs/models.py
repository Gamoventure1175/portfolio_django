from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    body = models.TextField()
    create_date = models.DateField(null=False, auto_now=True)
