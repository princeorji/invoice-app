from django.urls import path
from . import views
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('invoice_list/', views.invoice_list, name="invoice-list"),
    path('create_invoice/', views.create_invoice, name="create-invoice"),
]