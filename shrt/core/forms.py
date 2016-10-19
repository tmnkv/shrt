from django import forms

from core.models import URL


class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['primary',]
        