from django.shortcuts import render, redirect
from django.views import View
from django.db import IntegrityError
from django.forms.utils import ErrorList
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth import (authenticate,
                                 login,
                                 logout,
                                 )
from django.contrib.auth.models import User, Permission, Group
import json
from .forms import UserLoginForm, UserRegisterForm, CompanyRegisterForm, OffersSearchForm
from .models import Company
from joboffers.models import Offer
from django.db.models import Q




def logout_view(request):
    logout(request)
    return redirect('/')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {

            'form': form
        })

    def post(self, request):
        fail = 'Wrong username or password'
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        return render(request, self.template_name, {

            'form': form,
            'fail': fail
        })


# User register
class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'user_register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        try:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # Employee group adding
            group = Group.objects.get(name="user")
            user.groups.add(group)
            user.save()
            return redirect('/login')
        except IntegrityError:
            form._errors['username'] = ErrorList(['Username "{}" is already in use'.format(username)])

            return super(UserRegisterView, self).form_invalid(form)


#  Company register
class CompanyRegisterView(FormView):
    form_class = CompanyRegisterForm
    template_name = 'company_register.html'

    def form_valid(self, form):
        try:

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            company_name = form.cleaned_data['company_name']
            user = User(username=username, email=email, )
            user.set_password(password)
            user.save()
            employer = Company(user=user, company_name=company_name)
            employer.save()
            # Employee group adding
            group = Group.objects.get(name="company")
            user.groups.add(group)
            user.save()
            return redirect('/login')
        except IntegrityError:
            form._errors['username'] = ErrorList(['Username "{}" is already in use'.format(username)])

        return super(CompanyRegisterView, self).form_invalid(form)


class SearchJobView(FormView):
    template_name = 'homepage.html'
    form_class = OffersSearchForm

    def form_valid(self, form):
        position = form.cleaned_data['position']
        city = form.cleaned_data['city']
        offers_list = Offer.objects.filter(city__city__icontains=city).filter(position__icontains=position)
        return render(self.request, 'offers_list.html', {

            'offers_list': offers_list,
            'given_position': position,
            'given_city': city
        })

