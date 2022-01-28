from django.forms import ModelForm
from .models import Bill, Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'