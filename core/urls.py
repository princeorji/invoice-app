from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('invoice_list/', views.invoice_list, name="invoice-list"),
    path('create_invoice/', views.create_invoice, name="create-invoice"),
    path('invoice_detail/<int:pk>/', views.invoice_detail, name="invoice-detail"),
]