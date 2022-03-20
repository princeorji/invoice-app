from django import forms
from django.forms import ModelForm
from django.forms import formset_factory

from .models import Invoice, Service

class DateInput(forms.DateInput):
    input_type = 'date'

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ('uuid', 'owner',)

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {'due_date': DateInput}

ServiceFormSet = formset_factory(ServiceForm)