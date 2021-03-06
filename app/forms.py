from __future__ import unicode_literals, absolute_import

from datetime import datetime

from django import forms
from .models import Feature

__author__ = 'inspaya'


class FeatureForm(forms.ModelForm):
    """
    Custom Data Entry Form
    """
    class Meta:
        model = Feature
        fields = '__all__'

    def clean_target_date(self):
        target_date = self.cleaned_data['target_date']
        return datetime.strftime(target_date, '%Y-%m-%dT%H:%MZ')
