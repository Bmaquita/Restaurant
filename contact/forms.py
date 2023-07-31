from django import forms

from .models import Reservation


class Reservation(forms.ModelForm):

    class Meta:
        model = Reservation

        #importing all field the reservation model
        fields = "__all__"

        widgets = {
            'date':forms.DateInput(attrs={'type':'date'}),
            'time':forms.TimeInput(attrs={'type':'time'})

        }
