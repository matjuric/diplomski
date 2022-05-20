from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('statistics/', views.statistics, name='statistics'),
    path('add_new/', views.IncidentCreateView.as_view(), name='add_new'),
]