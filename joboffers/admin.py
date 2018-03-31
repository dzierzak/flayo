from django.contrib import admin
from .models import City, Certificate, Offer

myModels = [City, Certificate, Offer]

admin.site.register(myModels)

