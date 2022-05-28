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
    all_incidents = Incident.objects.all()
    labels_severity = ['LOW', 'MEDIUM', 'HIGH']
    labels_resolved = ['Resolved', 'Open']
    data_severity = [0, 0, 0]
    data_resolved = [0, 0]
    all_incidents = Incident.objects.all()
    for incident in all_incidents:
        if (incident.resolved == 'Y'):
            data_resolved[0] += 1
        else:
            data_resolved[1] += 1

        if (incident.severity == 'L'):
            data_severity[0] += 1
        elif (incident.severity == 'M'):
            data_severity[1] +=1
        else:
            data_severity[2] += 1

    return render(request, 'statistics.html', {
        'number_of_incidents': number_of_incidents,
        'all_incidents': all_incidents,
        'labels_severity': labels_severity,
        'labels_resolved': labels_resolved,
        'data_severity': data_severity,
        'data_resolved': data_resolved
    })

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
        'content',
        'needed_expertise',
        'user',
    )

    def get_success_url(self):
        return reverse_lazy('incident_details', kwargs={'pk': self.object.pk})

class IncidentCreateView(CreateView):
    model = Incident
    fields = ('name', 'spotted_by', 'user', 'date_spotted', 'severity', 'resolved', 'needed_expertise')
    success_url = 'success/'

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)
