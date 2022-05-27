from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.IncidentListView.as_view(), name='home'),
    path('statistics/', views.statistics, name='statistics'),
    path('add_new/', views.IncidentCreateView.as_view(), name='add_new'),
    path('add_new/success/', views.success, name='success'),
    path('<int:pk>/', views.DetailView.as_view(), name='incident_details'),
    path('<int:pk>/delete', views.IncidentDeleteView.as_view(), name='delete_incident_instance'),
    path('<int:pk>/update', views.IncidentUpdateView.as_view(), name='update_incident_instance')
]