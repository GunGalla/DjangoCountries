"""Django views file."""
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Country, Language


def index(request):
    """View for homepage."""
    return render(request, 'index.html')


def countries_list(request):
    """View to show all countries.txt."""
    countries = Country.objects.all()
    return render(request, 'countries_list.html', context={'countries': countries})


def country(request, country_name):
    """View of dedicated country."""
    try:
        country = Country.objects.get(name=country_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Country, named {country_name} not found :(")
    context = {'country': country}
    return render(request, 'country.html', context)


def languages(request):
    """View of all using languages."""
    languages = Language.objects.all()
    return render(request, 'languages.html', context={'languages': languages})
