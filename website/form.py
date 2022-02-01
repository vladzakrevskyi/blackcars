from django import forms
from .form import *


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-form'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact-form'}), required=False)


class SmallReservationForm(forms.Form):
    date_start = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_end = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class ReservationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    license = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pesel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    reservation_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls'}))
    selected = forms.CharField(widget=forms.TextInput(attrs={'class': 'select'}))
    price_day = forms.CharField(widget=forms.TextInput(attrs={'class': 'price_day'}))
    limit_day = forms.CharField(widget=forms.TextInput(attrs={'class': 'limit_day'}))
    extra_services = forms.CharField(widget=forms.TextInput(attrs={'class': 'extra_services'}))
    pay = forms.CharField(widget=forms.TextInput(attrs={'class': 'pays'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'card_data'}), required=False)
    card_month = forms.CharField(widget=forms.TextInput(attrs={'class': 'card_month'}), required=False)
    card_year = forms.CharField(widget=forms.TextInput(attrs={'class': 'card_year'}), required=False)
    card_cvv = forms.CharField(widget=forms.TextInput(attrs={'class': 'card_data'}), required=False)
    car_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls'}))
    date_start = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls'}))
    date_end = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls'}))
    rent_days = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls'}))
    actual_deposit = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls'}))
    rent_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls'}))
    final_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls'}))
    text_pay = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_pay_method'}))
    remarks = forms.CharField(widget=forms.Textarea(attrs={"rows":4}), required=False)


class NewsletterForm(forms.Form):
    email = forms.EmailField()
