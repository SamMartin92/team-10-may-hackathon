""" Imports required for home app """
from django.shortcuts import render


def index(request):
    """ Return homepage"""

    return render(request, 'index.html')


def resources(request):
    """ Return resources page"""

    return render(request, 'resources.html')
