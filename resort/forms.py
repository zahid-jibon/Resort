from tabnanny import check
from django import forms
from django.forms import ModelForm
from .models import (
    booking,
    saveContact,
)


class BookingForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
            'class': 'input',
			
			}))
    email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
            'class': 'input',
			
			}))

    number = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Phone number..',
            'class': 'input',

            }))

    check_in = forms.DateField(required=True,
        widget=forms.TextInput(attrs={  
            'placeholder': '*Check in date..',
            'type': 'date',
            'class': 'input',
            }))

    check_out = forms.DateField(required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Check out date..',
            'type': 'date',
            'class': 'input',
            }))

    room_price = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Room with price..',
            'class': 'input',
            }))


    class Meta:
        model = booking
        fields = ('name', 'email', 'number', 'check_in', 'check_out', 'room_price')




class SaveContactForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Full name..',
            'class': 'form-control',

            }))
    
    phone = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Phone number..',
            'class': 'form-control',
            }))
            
          
            
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..',
            'class': 'form-control',
            
            }))

    

    class Meta:
        model = saveContact
        fields = ('name' , 'phone', 'email')

   