from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Dive


class DiveForm(forms.ModelForm):
    """
    Sets model and fields for Dive form.
    Provides front-end user with Summernote widget.
    """
    class Meta:
        model = Dive
        fields = ('title', 'date', 'location', 'diving_site',
                  'duration', 'depth', 'gas_mixture', 'air_in',
                  'air_out', 'visibility', 'description')
        widgets = {
            'content': SummernoteWidget(),
        }
