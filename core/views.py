from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Client, Bill
from .forms import ClientForm, BillForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    clients = Client.objects.all()
    return render(request, 'dashboard.html', {'clients': clients})

def dash_detail(request, pk):
    client = Client.objects.get(pk=pk)
    return render(request, 'dash_details.html', {'client': client})

def create_invoice(request):
    f_client = ClientForm
    f_bill = BillForm

    if request.method == 'POST':
        f_client = ClientForm(request.POST or None)
        f_bill = BillForm(request.POST or None)
        if f_client.is_valid() or f_bill.is_valid():
            f_client.save()
            f_bill.save()
            return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'create_invoice.html', {
        'f_client': f_client,
        'f_bill': f_bill
    })

def update_invoice(request, pk):
    client = Client.objects.get(pk=pk)
    bill = Bill.objects.get(pk=pk)

    if request.method == 'POST':
        f_client = ClientForm(request.POST, instance=client)
        f_bill = BillForm(request.POST, instance=bill)
        if f_client.is_valid() or f_bill.is_valid():
            f_client.save()
            f_bill.save()
            return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'update_invoice.html', {
        'f_client': f_client,
        'f_bill': f_bill
    })

def delete_invoice(request, pk):
    client = Client.objects.get(pk=pk)
    bill = Bill.objects.get(pk=pk)

    if request.method == 'POST':
        client.delete()
        bill.delete()
        return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'delete_invoice.html', {
        'client': client,
        'bill': bill
    })

