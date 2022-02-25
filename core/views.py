from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Invoice, Service
from .forms import InvoiceForm, ServiceFormSet

# Create your views here.

def index(request):
    return render(request, 'index.html')

def invoice_list(request):
    invoice_list = Invoice.objects.all().order_by('-date')

    paginator = Paginator(invoice_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    search = invoice_list.filter(Q(date__icontains=q))

    context = {
        'invoice_list': invoice_list,
        'page_obj': page_obj,
        'search': search
    }
    return render(request, 'invoice-list.html', context)

def invoice_detail(request, pk):
    invoice = Invoice.objects.get(pk=pk)

    context = {
        'invoice': invoice,
    }
    return render(request, 'invoice-detail.html', context)

def create_invoice(request):
    formset = ServiceFormSet()
    form = InvoiceForm()

    if request.method == 'POST':
        formset = ServiceFormSet(request.POST)
        form = InvoiceForm(request.POST)
        if form.is_valid() and formset.is_valid():
            total = 0
            for form in formset:
                amount = float(formset.rate)*float(formset.quantity)
                total += amount
                formset.save()
            form.total_amount = total
            form.save()
            return redirect('invoice-list')

    context = {
        "formset": formset,
        "form": form,
    }
    return render(request, 'create-invoice.html', context)





