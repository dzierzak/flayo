from django import forms
from django.core.exceptions	import ValidationError
from django.contrib.auth.models import User


#    LOGIN


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

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
