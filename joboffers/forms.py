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
                      Field('city', placeholder='Offert title',
                           css_class="some-class"),
                      Field('country', placeholder='Offert title',
                           css_class="some-class"),
                     Fieldset('Description',
                          'description', placeholder='description',
                           css_class="some-class"),
                     Fieldset('Salaries',
                 Field('salary_from', placeholder='Offert title',
                   css_class="some-class"),
                 Field('salary_to', placeholder='Offert title',
                       css_class="some-class"),
                 Field('wage_per_hour_from', placeholder='Offert title',
                       css_class="some-class"),
                 Field('wage_per_hour_to', placeholder='Offert title',
                       css_class="some-class"),
                 Field('employment_status', placeholder='Offert title',
                      css_class="some-class")
                 ),
                     Fieldset('Requirements',
                              Field('experience', placeholder='Offert title',
                                    css_class="some-class"),
                              Field('requirements', placeholder='Offert title',
                                    css_class="some-class"),
                              Field('education_level', placeholder='Offert title',
                                    css_class="some-class"),
                              Field('certificates', placeholder='Offert title',
                                    css_class="some-class"),
                              ),
                     Fieldset('Benefits',
                              Field('benefits_description', placeholder='Offert title',
                                    css_class="some-class"),
                              ),
                     Fieldset('Additional',
                              Field('required_docs', placeholder='Offert title',
                                    css_class="some-class"),
                              Field('clause', placeholder='Offert title',
                                    css_class="some-class"),
                              Field('ref_number', placeholder='Offert title',
                                    css_class="some-class"),
                              ),
                    ))



