from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .models import Invoice
from .forms import InvoiceForm, ServiceFormSet

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

@login_required(login_url='account_login')
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

@login_required(login_url='account_login')
def invoice_detail(request, pk):
    invoice = Invoice.objects.get(pk=pk)

    return render(request, 'invoice-detail.html', {"invoice": invoice})

@login_required(login_url='account_login')
def create_invoice(request):
    form = InvoiceForm()
    formset = ServiceFormSet()

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
    return render(request, 'create-invoice.html', {"form": form, "formset": formset})





