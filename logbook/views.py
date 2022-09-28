from django.shortcuts import render
from django.views import generic, View
from .models import Dive


class DiveList(generic.ListView):
    model = Dive
    queryset = Dive.objects.all()
    template_name = 'logbook.html'
