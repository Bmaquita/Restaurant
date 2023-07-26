from django.db import models


# Create your models here
from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):

    #hoice field
    DRAFT = 'D'
    PUBLISHED = 'P'

    POST_STATUS = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    title = models.CharField(max_length=120)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(default= timezone.now(),auto_now_add=True)

    feature_image = models.ImageField(upload_to='Blog/Images', blank=True, null=True)

    post_status = models.CharField(max_length=1, choices=POST_STATUS, default=DRAFT)

    description = models.TextField()


class Category(models.Model):
    category = models.CharField(max_length=100)

