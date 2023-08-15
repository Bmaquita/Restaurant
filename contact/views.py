from django.shortcuts import render, redirect

from .forms import Reservation, ContactForm

from .models import ContactDetail

from django.core.mail import send_mail, BadHeaderError

from django.contrib import messages 

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

            messages.success(request, "Thank you, we'll get back to you as soon as possible")

            return redirect('contact')
        
        else:
            messages.error("There was an issues found while submiting form")
            
        
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

            messages.success(request, "Thank you for booking we'll get back to you as soon as possible!")

            return redirect('index')
        
        else:
            messages.success(request, "There was an error reserving you table")

    context = {

        'reservation_form':reservation_form

    }

    return render(request, 'reservation/reservation.html', context)