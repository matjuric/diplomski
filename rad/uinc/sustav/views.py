from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from httplib2 import Http

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

def success(request):
    return render(request, 'success.html')

def incident_details(request):
    return render(request, '')

class IncidentCreateView(CreateView):
    model = Incident
    fields = ('name', 'spotted_by', 'date_spotted', 'severity')
    success_url = 'success/'

    def form_valid(self, form) -> HttpResponse:
        form.save()
        # print(form)
        return super().form_valid(form)