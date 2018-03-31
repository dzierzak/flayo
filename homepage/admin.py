from django.contrib import admin
from .models import Company

myModels = [Company, ]

admin.site.register(myModels)