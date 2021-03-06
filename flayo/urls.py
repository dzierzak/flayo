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

from homepage.views import UserLoginView, UserRegisterView, CompanyRegisterView, logout_view, SearchJobHomepageView
from homepage.ajax import get_position, get_city
from joboffers.views import OfferAddView, OffersListView, OfferDetailsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         SearchJobHomepageView.as_view(), name="homepage-view"),
    path('add-offer/',
         OfferAddView.as_view(), name="offer-add-view"),
    path('offer/<int:pk>/', OfferDetailsView.as_view(), name='offer_details'),

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
    re_path(r'^api/get_position/', get_position, name='get_position'),
    re_path(r'^api/get_city/', get_city, name='get_city'),

]
