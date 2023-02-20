"""Django views file."""
from django.shortcuts import render
from django.http import HttpResponseNotFound
import json


def index(request):
    """View for homepage."""
    return render(request, 'index.html')


def countries_list(request):
    """View to show all countries.txt."""
    file = 'country-by-languages.json'
    with open(file, 'r') as countries_list:
        countries_json = countries_list.read()
    countries = json.loads(countries_json)
    return render(request, 'countries_list.html', context={'countries': countries})


def country(request, country_name):
    """View of dedicated country."""
    file = 'country-by-languages.json'
    with open(file, 'r') as countries_list:
        countries_json = countries_list.read()
    countries = json.loads(countries_json)
    for item in countries:
        if item['country'] == country_name:
            context = {'country': item}
            return render(request, 'country.html', context)
    return HttpResponseNotFound(f"Country, named {country_name} not found :(")
