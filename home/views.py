from django.shortcuts import render, redirect

from .models import Sliders, OurStory, Testimonials, Gallery, Services

from contact.models import ContactDetail

#import forms for reservation models 


#importing the reservation forms from reservation
# I had to create an instance of reservation forms here so that I' able to display it on the index template since the reservation is being hadled on a different app

from contact.forms import Reservation

# Create your views here.
def index(request):

    #instance of reservation
    reservation_form = Reservation()

    sliders = Sliders.objects.all()

    about =  OurStory.objects.all()

    testimonials = Testimonials.objects.all()

    gallery = Gallery.objects.all()

    services = Services.objects.all()

    contact_details = ContactDetail.objects.first()


    context = {
        'reservation_form':reservation_form,
        'sliders':sliders,
        'about':about,
        'testimonials':testimonials,
        'gallery':gallery, 
        'services':services,
        'contact_details':contact_details
    }
    
    return render(request,'home/index.html', context)

