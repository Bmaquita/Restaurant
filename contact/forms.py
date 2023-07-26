from django import forms

from .models import Reservation


class Reservation(forms.ModelForm):

    model = Reservation
    fields = "__all__"



class Contact(forms.Form):

    name = forms.CharField(max_length=100)

    email = forms.EmailField(required=False)

    phone = forms.CharField(max_length=16)

    message = forms.Textarea()