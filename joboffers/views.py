from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404

from django.utils import timezone
from django.views import View
from .models import Offer
from .forms import OfferAddForm, OffersSearchForm

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


# BROWSE OFFERS VIEW
class OffersListView(FormView):

    template_name = 'offers_list.html'
    form_class = OffersSearchForm

    def get_context_data(self, **kwargs):
        """Get view context dictionary."""
        context = super(OffersListView, self).get_context_data(**kwargs)
        context['offers_list'] = Offer.objects.all().order_by('-id')
        context['new'] = False
        return context

    def form_valid(self, form):
        position = form.cleaned_data['position']
        city = form.cleaned_data['city']
        offers_list = Offer.objects.filter(city__city__icontains=city).filter(position__icontains=position)
        return render(self.request, 'offers_list.html', {

            'offers_list': offers_list,
            'given_position': position,
            'given_city': city
        })


# OFFER DETAIL VIEW
class OfferDetailsView(DetailView):

    model = Offer

    def get_context_data(self, **kwargs):
        context = super(OfferDetailsView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template='offer_details.html',
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

