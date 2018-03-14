from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Offer(models.Model):

    # basic informations
    position = models.CharField(max_length=64, blank=False)
    # location
    city = models.CharField(max_length=128, blank=False)
    country = models.CharField(max_length=128, blank=False)
    # offer description
    description = models.CharField(max_length=9000)
    # salaries info
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    wage_per_hour = models.IntegerField()



    company_name = models.CharField(max_length=128)
    author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        help_text=_("When offer was created")
    )

    def __str__(self):
        return self.position


class Category(models.Model):
    name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.name
