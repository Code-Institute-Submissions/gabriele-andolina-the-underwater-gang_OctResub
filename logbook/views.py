from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Dive
from .forms import DiveForm


class DiveList(generic.ListView):
    """
    A view to show a list of all logged dives.
    """
    model = Dive
    queryset = Dive.objects.all()
    template_name = 'logbook.html'
    paginate_by = 6


class DiveDetails(LoginRequiredMixin, View):
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


class LogDive(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A view to allow users to log a dive in their logbook.
    """
    model = Dive
    form_class = DiveForm
    template_name = 'dive_form.html'
    success_url = '/'
    success_message = "Whale done! Your dive has been logged correctly."

    def form_valid(self, form):
        form.instance.diver = self.request.user
        return super().form_valid(form)


class UpdateDive(LoginRequiredMixin, SuccessMessageMixin,
                 UserPassesTestMixin, UpdateView):
    """
    A view to allow users to update a logged dive in their logbook.
    """
    template_name = 'dive_form.html'
    success_url = '/'
    success_message = "Krilliant! Your dive log has been updated successfully."

    model = Dive
    form_class = DiveForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        dive = self.get_object()
        if self.request.user == dive.diver:
            return True
        return False


class DeleteDive(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to allow users to delete a logged dive from their logbook.
    """
    template_name = 'dive_confirm_delete.html'
    success_url = '/'
    success_message = "Your dive has been deleted successfully!"

    model = Dive

    def test_func(self):
        dive = self.get_object()
        if self.request.user == dive.diver:
            return True
        return False
