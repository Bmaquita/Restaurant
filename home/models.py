from django.db import models

# Create your models here.


class Sliders(models.Model):
    
    slider = models.ImageField(upload_to='home/sliders', null=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):

        return str(self.slider)


class OurStory(models.Model):
    
    title = models.CharField(max_length=200)

    description = models.TextField()

    imageOne = models.ImageField(upload_to='home/our-story')
    imageTwo = models.ImageField(upload_to='home/our-story')
    imageThree = models.ImageField(upload_to='home/our-story')
    imageFour = models.ImageField(upload_to='home/our-story')

    chefName = models.CharField(max_length=100, null=True)
    chefTitle = models.CharField(max_length=100, null=True, blank=True)
    chef_image = models.ImageField(upload_to='home/Chef', null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Our Story'

    def __str__(self):

        return self.title

class Testimonials(models.Model):
    
    author = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):

        return self.author

class Gallery(models.Model):
    image = models.ImageField(upload_to='home/gallery')


    class Meta:
        verbose_name = verbose_name_plural = 'Gallery'


    def __str__(self):

        return str(self.image)


class Services(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    serviceImage = models.ImageField(upload_to='home/service')

    class Meta:
        verbose_name = "Service"
        
        verbose_name_plural = 'Services'


    def __str__(self):

        return self.title



    



