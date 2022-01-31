from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dash_detail/<int:pk>/', views.dash_detail, name="dash-detail"),
    path('create_client/', views.create_client, name="create-client"),
    path('create_bill/', views.create_bill, name="create-bill"),
    path('update_client/<int:pk>/', views.update_client, name="update-client"),
    path('update_bill/<int:pk>/', views.update_bill, name="update-bill"),
    path('delete_client_bill/<int:pk>/', views.delete_client_bill, name="delete-client-bill")

]