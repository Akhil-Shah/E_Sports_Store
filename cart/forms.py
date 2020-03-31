from django import forms

from .models import Feedback

class ShippingForm(forms.Form):

    country_choice = [
        ('', ''),
        ('india','India'),
        ('usa','USA'),
    ]

    state_choice = [
        ('', ''),
        ('maharashtra', 'Maharashtra'),
        ('gujurat', 'Gujurat'),
        ('tamil nadu', 'Tamil Nadu'),
        ('rajasthan', 'Rajasthan')
    ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":25}))
    phone = forms.IntegerField()
    country = forms.CharField(widget= forms.Select(choices=country_choice))
    state = forms.CharField(widget= forms.Select(choices=state_choice))
    city = forms.CharField()
    zip_code = forms.CharField()
    card_choices = [('1', 'Credit Card'), ('2', 'Debit Card')]
    choice_field = forms.ChoiceField(label="Payment Choice",choices=card_choices, widget=forms.RadioSelect)


class FeedbackForm(forms.ModelForm):

    purchase_id = forms.UUIDField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":25}))

    class Meta:
        model = Feedback
        fields = ['purchase_id', 'email', 'phone', 'feedback']


    

    