from django import forms
from django.urls import reverse, reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.layout import  Submit, Fieldset, Layout, Div
from django.utils.translation import ugettext_lazy as _
from .models import Offer


# JOBS
class OfferAddForm(forms.ModelForm):

    description = forms.CharField(
        label="Please, describe your job offer",
        required=True,
        widget=forms.Textarea()
    )

    salary_from = forms.IntegerField(
        required=False,
    )

    salary_to = forms.IntegerField(
        required=False,
    )

    wage_per_hour_from = forms.IntegerField(
        required=False,
    )

    wage_per_hour_to = forms.IntegerField(
        required=False,
    )

    requirements = forms.CharField(
        label="Please, describe your requirements",
        required=True,
        widget=forms.Textarea()
    )

    class Meta:
        model = Offer
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput
    }


class OffersSearchForm(forms.Form):
    position = forms.CharField(required=False)
    city = forms.CharField(required=False)
