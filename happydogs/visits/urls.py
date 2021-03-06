"""Visits urls."""

# Django
from django.urls import path
from django.views.generic import TemplateView

# Views
from .views import (
    get_visits_on_period,
    get_dogs_on_day,
)

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('visits/', get_visits_on_period, name='visits'),
    path('visits/<str:date>', get_dogs_on_day, name='detail'),
]
