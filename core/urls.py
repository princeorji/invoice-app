from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dash_detail/<int:pk>', views.dash_detail, name="dash_detail"),
    path('create_client/', views.create_client, name="create_client"),
    path('create_bill/', views.create_bill, name="create_bill"),

]