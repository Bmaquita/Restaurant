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
    
    """we can also create a slug field by overriding the save mode as it shows below
    In this scenario I could have not saved the author if would display an error saying Post with ID “None” doesn’t exist.

    This error might occur if you're trying to save a Post instance with an invalid or missing author. 
    
    """
    
    # def save(self, *args, **kwargs):
    

    
    #     if not self.slug: 

    #         self.slug = slugify(self.title)

    #Check if the object is being created (not updated) # Set the author to the currently logged-in user
    #     if not self.id:


    #This condition checks if the author_id attribute is not set, indicating that the author hasn't been assigned.
    #         if not self.author_id:

    #If both conditions are met, this line assigns the currently logged-in user as the author of the post. It uses the _get_current_user method to retrieve the user.
    #             self.author = self._get_current_user()
            


    #         return super().save(*args, **kwargs)


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category