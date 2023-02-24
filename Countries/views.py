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
    countries = Country.objects.all().order_by('name')
    return render(request, 'countries_list.html', context={'countries': countries})


def country(request, country_name):
    """View of dedicated country."""
    try:
        country = Country.objects.get(name=country_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Country, named {country_name} not found :(")
    context = {'country': country}
    return render(request, 'country.html', context)


def languages_list(request):
    """View of all using languages."""
    languages = Language.objects.all().order_by('name')
    return render(request, 'languages.html', context={'languages': languages})


def language(request, language_name):
    try:
        language = Language.objects.get(name=language_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Language, named {country_name} not found :(")
    context = {'language': language}
    return render(request, 'language.html', context)
