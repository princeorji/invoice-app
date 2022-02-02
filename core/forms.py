from turtle import textinput
from django import forms
from django.forms import TextInput, ModelForm
from .models import Bill, Client

class DateInput(forms.DateInput):
    input_type = 'date'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {'phone_number': TextInput(attrs={
            'placeholder': '+234'
            })}

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        widgets = {'pay_date': DateInput}

