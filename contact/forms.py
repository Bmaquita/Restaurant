from django import forms

from .models import Reservation


class ContactForm(forms.Form):
    
    name = forms.CharField(required=True)

    email = forms.EmailField(required=True)

    subject = forms.CharField(max_length=100)

    phone = forms.CharField(required=False, max_length=18)

    message = forms.CharField(widget=forms.Textarea)

class Reservation(forms.ModelForm):

    class Meta:
        model = Reservation

        #importing all field the reservation model
        fields = "__all__"


        #editing the form fiels  -> This will add a date and time picker on this both form fields which initially would not give 
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'}),
            'time':forms.TimeInput(attrs={'type':'time'})

        }
