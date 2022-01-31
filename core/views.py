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

def create_client(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('create-bill'))
    return render(request, 'create_client.html', {'form': form})

def create_bill(request):
    form = BillForm()

    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form = Client.objects.create()
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'create_bill.html', {'form': form})

def update_client(request, pk):
    client = Client.objects.get(pk=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            return HttpResponseRedirect(reverse('update-bill'))
    return render(request, 'update_client.html', {'form': form})

def update_bill(request, pk):
    bill = Bill.objects.get(pk=pk)
    form = BillForm(instance=bill)

    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save(commit=False)
            form = Client.objects.create()
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'update_bill.html', {'form': form})

def delete_client_bill(request, pk):
    client = Client.objects.get(pk=pk)
    bill = Bill.objects.get(pk=pk)

    if request.method == 'POST':
        client.delete()
        bill.delete()
        return HttpResponseRedirect(reverse('dashboard'))
    context = {
        'client': client,
        'bill': bill
    }
    return render(request, 'delete_client_bill.html', context)

