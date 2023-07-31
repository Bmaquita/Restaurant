from django.shortcuts import render, redirect

from .forms import Reservation

# Create your views here.


from contact.forms import Reservation

def reservation(request):

    reservation_form = Reservation()

    if request.method == "POST":

        reservation_form = Reservation(request.POST)

        if reservation_form.is_valid():
            
            reservation_form.save()

            return redirect('index')

    context = {

        'reservation_form':reservation_form

    }

    return render(request, 'reservation/reservation.html', context)