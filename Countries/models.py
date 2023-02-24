"""Models module."""
from django.db import models


class Language(models.Model):
    """Language model."""
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f'language:{self.name}'


class Country(models.Model):
    """Country model."""
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Language, related_name='countries')

    def __repr__(self):
        return f'country:{self.name}'
