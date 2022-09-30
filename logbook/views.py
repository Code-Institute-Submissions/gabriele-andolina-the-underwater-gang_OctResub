from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Dive


class DiveList(generic.ListView):
    model = Dive
    queryset = Dive.objects.all()
    template_name = 'logbook.html'


class DiveDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Dive.objects.all()
        dive = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'dive_details.html',
            {
                'dive': dive,
            },
        )
