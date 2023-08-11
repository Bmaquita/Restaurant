from django.shortcuts import render

from .models import Sliders, OurStory, Testimonials, Gallery, Services

from contact.models import ContactDetail

from meals.models import Meal


#importing the reservation forms from reservation
# I had to create an instance of reservation forms here so that I' able to display it on the index template since the reservation is being hadled on a different app

from contact.forms import Reservation

# Create your views here.
def index(request):

    #instance of reservation - contact app
    reservation_form = Reservation()
    contact_details = ContactDetail.objects.first()

    #instances of home app
    sliders = Sliders.objects.all()

    about =  OurStory.objects.all()

    testimonials = Testimonials.objects.all()

    gallery = Gallery.objects.all()

    services = Services.objects.all()

    #instances of meals app
    specials = Meal.objects.filter(on_special=True)



    


    context = {
        'reservation_form':reservation_form,
        'contact_details':contact_details,
        'sliders':sliders,
        'about':about,
        'testimonials':testimonials,
        'gallery':gallery, 
        'services':services,
        'specials':specials
    }
    
    return render(request,'home/index.html', context)

