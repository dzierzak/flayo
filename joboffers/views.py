from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views import View
from .models import JobOffer
from .forms import *


class AddJobView(LoginRequiredMixin, CreateView):
    login_url = '/login'

    model = JobOffer
    form_class = AddJobForm
    template_name = 'joboffer_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return redirect('/')