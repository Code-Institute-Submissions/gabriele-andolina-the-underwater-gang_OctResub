from django import forms
from .models import Dive


class DiveForm(forms.ModelForm):
    """
    Sets model and fields for Dive form.
    """
    class Meta:
        model = Dive
        fields = ('title', 'date', 'location', 'diving_site',
                  'duration', 'depth', 'gas_mixture', 'air_in',
                  'air_out', 'visibility', 'description')
