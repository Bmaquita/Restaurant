from django.db import models

# Create your models here.

class Reservation(models.Model):
    
    name = models.CharField(max_length=100)

    email = models.EmailField(nul=True, blank=True)

    phone = models.CharField(max_length=16)

    person = models.IntegerField()

    date = models.DateField()

    time = models.TimeField()

    

    class Meta:
        
        verbose_name = 'Reservation'

        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.name