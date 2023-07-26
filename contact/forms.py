from django import forms 

class Reservation(forms.Form):
    
    name = forms.CharField(max_length=100)

    email = forms.EmailField(required=False)

    phone = forms.CharField(max_length=16)

    person = forms.IntegerField()

    date = forms.DateField()

    time = forms.TimeField()


class Contact(forms.Form):

    name = forms.CharField(max_length=100)

    email = forms.EmailField(required=False)

    phone = forms.CharField(max_length=16)

    message = forms.Textarea()