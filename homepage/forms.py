from django import forms
from django.core.exceptions	import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.layout import  Submit, Fieldset, Layout, Div
from django.contrib.auth.models import User


#    LOGIN


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

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


#    REGISTER


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    email_confirm = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [

            'username',
            'email',
            'email_confirm',
            'password',
            'password_confirm'

                  ]

    def clean(self):
        print(self.cleaned_data)

        email = self.cleaned_data['email']
        email_confirm = self.cleaned_data['email_confirm']

        if email != email_confirm:
            raise forms.ValidationError("Emails must match")

        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError("Passwords must match")

        return self.cleaned_data


class CompanyRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    email_confirm = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    company_name = forms.CharField()

    def clean(self):
        print(self.cleaned_data)

        email = self.cleaned_data['email']
        email_confirm = self.cleaned_data['email_confirm']

        if email != email_confirm:
            raise forms.ValidationError("Emails must match")

        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError("Passwords must match")

        return self.cleaned_data
