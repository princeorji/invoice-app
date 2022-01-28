from django.forms import ModelForm
from django import forms

from .models import Client
from .widgets import FengyuanChenDatePickerInput

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class DateForm(forms.Form):
    item = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    rate = forms.DecimalField(max_digits=8, decimal_places=2)
    hours = forms.IntegerField(default=1)
    pay_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'], 
        widget=FengyuanChenDatePickerInput()
    )