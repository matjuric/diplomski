from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView

from .models import Incident

# Create your views here.

def statistics(request):
    number_of_incidents = Incident.objects.count()
    context = {'number_of_incidents': number_of_incidents}
    return render(request, 'statistics.html', context)

def success(request):
    return render(request, 'success.html')

class IncidentListView(ListView):
    model = Incident

class DetailView(generic.DetailView):
    model = Incident

class IncidentDeleteView(DeleteView):
    model = Incident
    success_url = "/sustav/home"

class IncidentUpdateView(UpdateView):
    model = Incident
    fields = (
        'severity',
        'resolved',
    )
    success_url = "/sustav/home"

class IncidentCreateView(CreateView):
    model = Incident
    fields = ('name', 'spotted_by', 'date_spotted', 'severity', 'resolved')
    success_url = 'success/'

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)