from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Client, Bill
from .forms import ClientForm, BillForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def invoice_list(request):
    clients = Client.objects.all()
    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    client_search = clients.filter(Q(name__icontains=q))

    context = {
        'clients': clients,
        'page_obj': page_obj,
        'client_search': client_search
    }
    return render(request, 'invoice_list.html', context)

def invoice_detail(request, pk):
    client = Client.objects.get(pk=pk)
    bill = Bill.objects.filter(client=client)
    context = {
        'client': client,
        'bill': bill
    }
    return render(request, 'invoice_detail.html', context)

def create_invoice(request):
    f_client = ClientForm
    f_bill = BillForm

    if request.method == 'POST':
        f_client = ClientForm(request.POST or None)
        f_bill = BillForm(request.POST or None)
        if f_client.is_valid() or f_bill.is_valid():
            f_client.save()
            f_bill.save()
            return redirect('core:index')
    context = {
        'f_client': f_client,
        'f_bill': f_bill
    }
    return render(request, 'cru_invoice.html', context)

def update_invoice(request, pk):
    client = Client.objects.get(pk=pk)
    bill = Bill.objects.get(pk=pk)

    f_client = ClientForm(instance=client)
    f_bill = BillForm(instance=bill)

    if request.method == 'POST':
        f_client = ClientForm(request.POST, instance=client)
        f_bill = BillForm(request.POST, instance=bill)
        if f_client.is_valid() or f_bill.is_valid():
            f_client.save()
            f_bill.save()
            return redirect('core:index')
    context = {
        'f_client': f_client,
        'f_bill': f_bill
    }
    return render(request, 'cru_invoice.html', context)

def delete_invoice(request, pk):
    client = Client.objects.get(pk=pk)
    bill = Bill.objects.get(pk=pk)

    if request.method == 'POST':
        client.delete()
        bill.delete()
        return redirect('core:index')
    context = {
        'client': client,
        'bill': bill
    }
    return render(request, 'delete_invoice.html', context)

