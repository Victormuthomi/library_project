from django.shortcuts import render

from django.views.generic import ListView

from .models import Worker 

# Create your views here.

class Workerlistview(ListView):
    model = Worker

