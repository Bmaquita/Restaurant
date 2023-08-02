from django.db import models



class ContactDetail(models.Model):

    restaurante_name = models.CharField(max_length=100)

    address = models.CharField(max_length=200)

    phone_number = models.CharField(max_length=18)

    fax = models.CharField(max_length=20)

    email = models.EmailField()

    facebook_link = models.URLField(null=True, blank=True)

    instagram_link = models.URLField(null=True, blank=True)

    twitter_link = models.URLField(null=True, blank=True)

    linkedin_link = models.URLField(null=True, blank=True)

    def __str__(self):
        
        return self.restaurante_name


class Reservation(models.Model):
    
    name = models.CharField(max_length=100)

    email = models.EmailField(null=True, blank=True)

    phone = models.CharField(max_length=16)

    person = models.IntegerField()

    date = models.DateField()

    time = models.TimeField()

    

    class Meta:
        
        verbose_name = 'Reservation'

        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.name