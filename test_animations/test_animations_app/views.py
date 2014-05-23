from django.shortcuts import render
from django.conf import settings
# Create your views here.

def index(request):
    if settings.TEMPLATE_DIRS:
        pass
    return render(request, 'index.html')