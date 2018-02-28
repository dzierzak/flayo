from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views import View
from .models import Offer
from .forms import OfferAddForm


class OfferAddView(LoginRequiredMixin, CreateView):
    login_url = '/login'

    model = Offer
    form_class = OfferAddForm
    template_name = 'offer_add.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return redirect('/')


# BROWSE OFFERTS VIEW
class OffersListView(View):
    def get(self, request):
        return render(request, 'offers_list.html', {

            'offers_list': Offer.objects.all().order_by('-id')
})