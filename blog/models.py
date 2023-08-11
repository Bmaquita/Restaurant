from django.db import models


from django.utils.text import slugify 

# Create your models here
from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):

    #choice field
    DRAFT = 'D'
    PUBLISHED = 'P'

    POST_STATUS = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    title = models.CharField(max_length=120)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(default= timezone.now)

    feature_image = models.ImageField(upload_to='Blog/Images', blank=True, null=True)

    post_status = models.CharField(max_length=1, choices=POST_STATUS, default=DRAFT)

    description = models.TextField()

    slug = models.SlugField(null=True, unique=True)

    class Meta:
        verbose_name = "Post"

        verbose_name_plural = "Posts"

    def __str__(self):

        return self.title

class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category