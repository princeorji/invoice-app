from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Client
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
            return HttpResponseRedirect(reverse('create_bill'))
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
