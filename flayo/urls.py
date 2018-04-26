"""Flayo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from homepage.views import HomepageView, UserLoginView, UserRegisterView, CompanyRegisterView, logout_view
from joboffers.views import OfferAddView, OffersListView, OfferDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         HomepageView.as_view(), name="homepage-view"),
    path('add-offer/',
         OfferAddView.as_view(), name="offer-add-view"),
    re_path(r'^offer/(?P<pk>(\d)+)',
         OfferDetailsView.as_view(), name="offert-details"),
    path('login/',
         UserLoginView.as_view(), name="login-view"),
    path('signupu/',
         UserRegisterView.as_view(), name="signupu-view"),
    path('signupc/',
         CompanyRegisterView.as_view(), name="signupc-view"),
    path('offers-list/',
         OffersListView.as_view(), name="offers-list-view"),
    path('logout/',
         logout_view, name="logout-view"),
]
