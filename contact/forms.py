from django import forms

from .models import Reservation


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
