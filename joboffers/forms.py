from django import forms
from django.urls import reverse, reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.layout import  Submit, Fieldset, Layout, Div
from . import validators
from .models import Offer


# JOBS
class OfferAddForm(forms.ModelForm):
    salary = forms.IntegerField(validators=[validators.validate_salary])
    description = forms.CharField(
        label="Please, describe your job offer",
        required=False,
        widget=forms.Textarea()
    )

    class Meta:
        model = Offer
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput
    }

    def __init__(self, *args, **kwargs):
        super(OfferAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-personal-data-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse_lazy('offer-add-view')
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset('Basic info',
                     Field('position', placeholder='Offert title',
                           css_class="some-class"),
                     Field('city', placeholder='Salary',
                           css_class="some-class"),
                     Field('country', placeholder='place of work',
                           css_class="some-class"),
                     ),
            TabHolder(Tab('Description', 'description'),
                      Tab('Company description', 'company_name')))

