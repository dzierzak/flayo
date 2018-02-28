from django import forms
from . import validators
from .models import Offer


# JOBS
class OfferAddForm(forms.ModelForm):
    salary = forms.IntegerField(validators=[validators.validate_salary])

    class Meta:
        model = Offer
        fields = '__all__'
        widgets = {
            'description': forms.Textarea,
            'author': forms.HiddenInput
}