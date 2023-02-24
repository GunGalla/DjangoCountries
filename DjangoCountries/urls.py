"""Django urls file."""
from django.contrib import admin
from django.urls import path
from Countries import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries-list/countries_by_letter/<str:letter>/', views.country_by_letter, name='letter'),
    path('countries-list/<str:country_name>/', views.country, name='distinct_country'),
    path('countries-list/', views.countries_list, name='countries_list'),
    path('languages/<str:language_name>/', views.language, name='distinct_language'),
    path('languages/', views.languages_list, name='languages_list'),
    path('admin/', admin.site.urls, name='admin'),
]
