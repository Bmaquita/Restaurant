from django.shortcuts import render

from .models import Sliders, OurStory, Testimonials, Gallery, Services

# Create your views here.
def index(request):

    sliders = Sliders.objects.all()

    about =  OurStory.objects.all()

    testimonials = Testimonials.objects.all()

    gallery = Gallery.objects.all()

    services = Services.objects.all()

    context = {
        'sliders':sliders,
        'about':about,
        'testimonials':testimonials,
        'gallery':gallery, 
        'services':services
    }
    
    return render(request,'home/index.html', context)