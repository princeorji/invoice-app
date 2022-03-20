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
    invoice_list = Invoice.objects.all().order_by('-created_on')
    paginator = Paginator(invoice_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    search = invoice_list.filter(Q(status__icontains=q))

    context = {
        'invoice_list': invoice_list,
        'page_obj': page_obj,
        'search': search
    }
    return render(request, 'invoice/invoice_item_view.html', context)

@login_required(login_url='account_login')
def create_invoice(request):
    form = InvoiceForm()
    formset = ServiceFormSet()

    if request.method == 'POST':
        formset = ServiceFormSet(request.POST)
        form = InvoiceForm(request.POST)
        if form.is_valid() and formset.is_valid():
            for form in formset:
                formset.save()
            form.save()
            return redirect('invoice-list')
    context = {
        'form': form,
        'formset': formset
    }
    return render(request, 'invoice/invoice_item_form.html', context)