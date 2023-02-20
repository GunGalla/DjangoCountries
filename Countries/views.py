"""Django views file."""
from django.shortcuts import render


def index(request):
    """View for homepage."""
    return render(request, 'index.html')
