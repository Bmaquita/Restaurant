from django.shortcuts import render

from .models import Sliders, OurStory

# Create your views here.
def index(request):

    sliders = Sliders.objects.all()

    about =  OurStory.objects.all()
    context = {
        'sliders':sliders,
        'about':about
    }
    
    return render(request,'home/index.html', context)