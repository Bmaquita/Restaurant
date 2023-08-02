from django.contrib import admin


from .models import Reservation, ContactDetail
# Register your models here.
admin.site.register([Reservation, ContactDetail])