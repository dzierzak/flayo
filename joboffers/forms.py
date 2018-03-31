from django import forms
from django.urls import reverse, reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.layout import  Submit, Fieldset, Layout, Div
from django.utils.translation import ugettext_lazy as _
from . import validators
from .models import Offer


# JOBS
class OfferAddForm(forms.ModelForm):
    description = forms.CharField(
        label="Please, describe your job offer",
        required=False,
        widget=forms.Textarea()
    )
    requirements = forms.CharField(
        label="Please, describe your requirements",
        required=False,
        widget=forms.Textarea()
    )

    company_description = forms.CharField(
        label="Please, describe your company",
        required=False,
        widget=forms.Textarea()
    )

    benefits_description = forms.CharField(
        label="Please, describe your benefits",
        required=False,
        widget=forms.Textarea()
    )

    salary_from = forms.IntegerField(validators=[validators.validate_salary])

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
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset('Basic info',
                      Field('position', placeholder='Offert title',
                            css_class="some-class"),
                      Field('city', placeholder='Salary',
                            css_class="some-class"),
                      Field('country', placeholder='place of work',
                            css_class="some-class")),
                      Tab('Description',
                          'description',
                          ),
                      Tab('Salary info',
                          'salary_from',
                          'salary_to',
                          'employment_status',
                          'working_hours'
                          ),
                      Tab('Requirements',
                          'requirements',
                          'experience',
                          'education_level',
                          'certificates'
                          ),
                      Tab('Company description',
                          'company_name',
                          'company_description',
                          'benefits_description',
                          ),
                      Tab('Additional info',
                          'required_docs',
                          'clause',
                          'ref_number',
                          ),
                     Submit('submit_button',
                        _('Save')),
        )


