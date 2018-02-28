from django.db import models
from django.contrib.auth.models import User


class Offer(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=9000)
    salary = models.IntegerField()
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
