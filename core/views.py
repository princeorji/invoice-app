from django.shortcuts import render, redirect
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

def create_bill(request):
    f_client = ClientForm()
    f_bill = BillForm()

    if request.method == 'POST':
            f_client = ClientForm(request.POST)
            if f_client.is_valid():
                f_client.save()

    if request.method == 'POST':
            f_bill = ClientForm(request.POST)
            if f_bill.is_valid():
                f_bill.save()
                return redirect('dashboard')
    context = {
        'f_client': f_client,
        'f_bill': f_bill
    }
    return render(request, 'create_bill.html', context)
