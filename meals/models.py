from django.db import models

# Create your models here.


#meals models 

class Meal(models.Model):

    name = models.CharField(max_length=200,unique=True)
    
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(decimal_places=2, max_digits=9999)

    on_special = models.BooleanField(default=False)

    on_special_price = models.DecimalField(decimal_places=2, max_digits=9999)

    feature_image = models.ImageField(upload_to='Meals/Feature-Image')

    slug = models.SlugField()

    description = models.TextField()

    class Meta:
        verbose_name = 'Meal'

        verbose_name_plural = 'Meals'

    
    def __str__(self):

        return self.name 



#category class

class Category(models.Model):

    category = models.CharField(max_length=50, unique=True)


    class Meta:
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

