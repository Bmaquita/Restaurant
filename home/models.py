from django.db import models

# Create your models here.


class Sliders(models.Model):
    
    slider = models.ImageField(upload_to='home/sliders', null=True)


class OurStory(models.Model):
    
    title = models.CharField(max_length=200)

    description = models.TextField()

    imageOne = models.ImageField(upload_to='home/our-story')
    imageTwo = models.ImageField(upload_to='home/our-story')
    imageThree = models.ImageField(upload_to='home/our-story')
    imageFour = models.ImageField(upload_to='home/our-story')


class Testimonials(models.Model):
    
    author = models.CharField(max_length=100)
    description = models.TextField()

class Gallery(models.Model):
    imageOne = models.ImageField(upload_to='home/gallery')
    imageTwo = models.ImageField(upload_to='home/gallery')
    imageThree = models.ImageField(upload_to='home/gallery')
    imageFour = models.ImageField(upload_to='home/gallery')


class Services(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    serviceImage = models.ImageField(upload_to='home/service')



