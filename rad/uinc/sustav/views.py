from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Incident

# Create your views here.

def home(request):
    incidents = Incident.objects.all()
    context = {'all_incidents': incidents}
    return render(request, 'home.html', context)

def statistics(request):
    number_of_incidents = Incident.objects.count()
    context = {'number_of_incidents': number_of_incidents}
    return render(request, 'statistics.html', context)

class IncidentCreateView(CreateView):
    model = Incident
    fields = ('name', 'spotted_by', 'date_spotted', 'severity')