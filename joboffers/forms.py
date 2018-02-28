from django import forms
from . import validators
from .models import JobOffer


# JOBS
class AddJobForm(forms.ModelForm):
    salary = forms.IntegerField(validators=[validators.validate_salary])

    class Meta:
        model = JobOffer
        fields = '__all__'
        widgets = {
            'description': forms.Textarea,
            'author': forms.HiddenInput
}