"""Django views file."""
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Country, Language

ALPHABET = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'


def index(request):
    """View for homepage."""
    return render(request, 'index.html')


def countries_list(request):
    """View to show all countries.txt."""
    countries = Country.objects.all().order_by('name')
    paginator = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'countries_list.html', context={
        'page_obj': page_obj,
        'alphabet': ALPHABET,
    })


def country(request, country_name):
    """View of dedicated country."""
    try:
        country = Country.objects.get(name=country_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Country, named {country_name} not found :(")
    context = {'country': country}
    return render(request, 'country.html', context)


def country_by_letter(request, letter):
    # TODO: 19-ое задание выполнено не совсем верно. Алфавит - по сути является фильтром.
    #   Но при переходе по выбранной букве - алфавит исчезает.
    #   В самом задании дан пример, там видно как должна работать фильтрация по алфавиту.
    countries = Country.objects.filter(name__startswith=letter)
    context = {'countries': countries, 'letter': letter}
    return render(request, 'letter.html', context)


def languages_list(request):
    """View of all using languages."""
    languages = Language.objects.all().order_by('name')
    return render(request, 'languages.html', context={'languages': languages})


def language(request, language_name):
    # TODO: если пройти по url: http://127.0.0.1:8000/languages/test/, то сайт падает с 500 ошибкой. Исправьте.
    try:
        language = Language.objects.get(name=language_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Language, named {country_name} not found :(")
    context = {'language': language}
    return render(request, 'language.html', context)
