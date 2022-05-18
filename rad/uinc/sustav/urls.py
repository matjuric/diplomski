from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('statistics/', views.statistics, name='statistics'),
    path('create_new/', views.IncidentCreateView.as_view(), name='create_new'),
]