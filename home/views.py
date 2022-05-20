from django.shortcuts import render

# Create your views here.
def index(request):
    """ Return homepage"""

    return render(request, 'index.html')

def resources(request):
    """ Return resources page"""

    return render(request, 'resources.html')