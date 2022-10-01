from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import Dive
from .forms import DiveForm


class DiveList(generic.ListView):
    """
    A view to show a list of all logged dives.
    """
    model = Dive
    queryset = Dive.objects.all()
    template_name = 'logbook.html'


class DiveDetails(View):
    """
    A view to show the full details for each logged dive.
    """
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


class LogDive(CreateView):
    """
    A view to allow users to log a dive in their logbook.
    """
    model = Dive
    form_class = DiveForm
    template_name = 'dive_form.html'
    success_url = '/'
    success_message = "Whale done! Your dive has been logged correctly."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
