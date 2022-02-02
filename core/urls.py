from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_invoice/', views.create_invoice, name="create-invoice"),
    path('update_invoice/<int:pk>/', views.update_invoice, name="update-invoice"),
    path('delete_invoice/<int:pk>/', views.delete_invoice, name="delete-invoice")

]