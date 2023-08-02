from django.shortcuts import render, redirect

from .forms import Reservation, ContactForm

from .models import ContactDetail

from django.core.mail import send_mail, BadHeaderError

from django.http import HttpResponse, HttpResponseRedirect

def contact(request):

    contact_details = ContactDetail.objects.first()
    
    
    contact_form = ContactForm()

    if request.method == 'POST':

        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():

            name = contact_form.cleaned_data['name']

            email = contact_form.cleaned_data['email']

            subject = contact_form.cleaned_data['subject']

            phone = contact_form.cleaned_data['phone']

            message = contact_form.cleaned_data['message']

            from_email = f'{email} <{name}> | {phone}'

            send_mail(subject, message,from_email, ["dinomaquita@gmail.com"], fail_silently=False)
            
        
    context = {
        'contact_form':contact_form,
        'contact_details':contact_details,
    }
    return render(request, 'contact/contact.html', context)



# Create your views here.
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