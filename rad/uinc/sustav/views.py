from django.http import HttpResponse
from django.shortcuts import render

from .models import Incident

# Create your views here.

def home(request):
    incidents = Incident.objects.all()
    context = {'all_incidents': incidents}
    # print('tu sam')
    return render(request, 'home.html', context)

def info(request):
    number_of_incidents = Incident.objects.count()
    context = {'number_of_incidents': number_of_incidents}
    return render(request, 'info.html', context)