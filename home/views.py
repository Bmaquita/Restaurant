from django.shortcuts import render, redirect

from .models import Sliders, OurStory, Testimonials, Gallery, Services

#import forms for reservation models 

from contact.forms import Reservation

# Create your views here.
def index(request):

    reservation_form = Reservation()

    sliders = Sliders.objects.all()

    about =  OurStory.objects.all()

    testimonials = Testimonials.objects.all()

    gallery = Gallery.objects.all()

    services = Services.objects.all()


    context = {
        'reservation_form':reservation_form,
        'sliders':sliders,
        'about':about,
        'testimonials':testimonials,
        'gallery':gallery, 
        'services':services,
    }
    
    return render(request,'home/index.html', context)

