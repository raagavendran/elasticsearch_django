from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blogpost')
    posted_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
