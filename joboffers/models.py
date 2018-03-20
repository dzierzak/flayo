from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
    city = models.CharField(max_length=64)
    city_english = models.CharField(max_length=64)

    def __str__(self):
        return self.city


class Certificate(models.Model):
    certificate = models.CharField(max_length=64)
    certificate_english = models.CharField(max_length=64)

    def __str__(self):
        return self.certificate


class Offer(models.Model):
    # basic informations
    position = models.CharField(max_length=64)
    # location
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    country = models.CharField(max_length=64)
    # offer description
    description = models.CharField(max_length=9000)
    # salaries info
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    wage_per_hour = models.IntegerField()
    employment_status = models.CharField(max_length=64)
    working_hours = models.CharField(max_length=64)
    # requirements
    experience = models.IntegerField()
    requirements = models.CharField(max_length=9000)
    education_level = models.CharField(max_length=64)
    certificates = models.ForeignKey(Certificate, on_delete=models.PROTECT)
    # benefits
    benefits_description = models.CharField(max_length=9000)
    # company
    company_description = models.CharField(max_length=9000)
    company_name = models.CharField(max_length=128)

    # additional informations
    required_docs = models.CharField(max_length=64)
    clause = models.CharField(max_length=512)
    ref_number = models.CharField(max_length=64)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        help_text=_("When offer was created")
    )

    def __str__(self):
        return self.position

#
# class Category(models.Model):
#     name = models.CharField(max_length=64, blank=False)
#
#     def __str__(self):
#         return self.name
#
#
# class Subcategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=64, blank=False)
#
#     def __str__(self):
#         return self.name