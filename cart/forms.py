from django import forms

class ShippingForm(forms.Form):

    country_choice = [
        ('india','India'),
        ('china','China'),
    ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    country = forms.CharField(widget= forms.Select(choices=country_choice))
    state = forms.CharField()
    city = forms.CharField()
    zip_code = forms.CharField()
    

    