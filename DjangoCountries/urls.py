"""Django urls file."""
from django.contrib import admin
from django.urls import path
from Countries import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries-list/<str:country_name>/', views.country, name='distinct_country'),
    path('countries-list/', views.countries_list, name='countries_list'),
    path('admin/', admin.site.urls, name='admin'),
]
