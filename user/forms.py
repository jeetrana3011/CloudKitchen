from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *




class CustomerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name','email', 'password1','password2','Phone_no','Address')

    Widget={

        'username': forms. TextInput (attrs= {'class': 'form-control', 'placeholder': 'username'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        'last_name': forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        'email': forms.EmailInput (attrs={'class': 'form-control', 'placeholder': 'Email'}), 
        'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), 
        'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
        'Phone_no': forms.NumberInput(attrs= {'class': 'form-control', 'placeholder': 'Phonenumber'}),
        'Address': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'address'}),
       



    }
class RestaurantRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1','password2','Restaurant_name','Website','Address')
        

    Widgets ={
                
        'username': forms. TextInput (attrs= {'class': 'form-control', 'placeholder': 'username'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        'last_name': forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        'email': forms.EmailInput (attrs={'class': 'form-control', 'placeholder': 'Email'}), 
        'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), 
        'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
        'Rerstaurant_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Restaurant Name'}),
        'Website': forms.TextInput(attrs={'class':'form-control','placeholder':'Restaurant Website'}), 
        'Address': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'address'}),
        
            }
    
   

   



       