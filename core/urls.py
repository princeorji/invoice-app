from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dash_detail/<int:pk>/', views.dash_detail, name="dash-detail"),
    path('create_invoice/', views.create_invoice, name="create-invoice"),
    path('update_invoice/<int:pk>/', views.update_invoice, name="update-invoice"),
    path('delete_invoice/<int:pk>/', views.delete_invoice, name="delete-invoice")

]