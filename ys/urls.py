from django.urls import path
from . import views

urlpatterns = [
    path('', views.ys_summary, name='ys_summary'),
]
