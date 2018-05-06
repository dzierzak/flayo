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
    # Countries
    POLAND = 'Poland'
    UK = 'United Kingdom'
    GERMANY = 'Germany'

    COUNTRIES_CHOICES = (
        (POLAND, _('Poland')),
        (UK, _('United Kingdom')),
        (GERMANY, _('Germany'))
    )

    # Employment statuses
    CONTRACT_WITH_NO_PERIOD = "CONTRACT WITH NO PERIOD"
    CONTRACT_WITH_PERIOD = "Employment contract for a specified period/fixed term"
    B2B = "B2B agreement"
    CONTRACT_FOR_SPECIFIC = "Project delivery contract"

    EMPLOYMENT_STATUSES_CHOICES = (
        (CONTRACT_WITH_NO_PERIOD, _('Employment contract for an unspecified period')),
        (CONTRACT_WITH_PERIOD, _('Employment contract for a specified period/fixed term')),
        (B2B, _('B2B agreement')),
        (CONTRACT_FOR_SPECIFIC, _('Project delivery contract'))
    )

    # Education level
    PRIMARY = 'Primary education'
    SECONDARY = 'Secondary education'
    HIGHER_EDUCATION = 'Higher education'

    EDUCATION_LEVEL_CHOICES = (
        (PRIMARY, _('Primary education')),
        (SECONDARY, _('Secondary education')),
        (HIGHER_EDUCATION, _('Higher education'))
    )

    # basic informations
    position = models.CharField(max_length=64)
    # location
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    country = models.CharField(max_length=64, choices=COUNTRIES_CHOICES, default=POLAND)
    # offer description
    description = models.CharField(max_length=9000, null=True)
    # salaries info
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    wage_per_hour_from = models.IntegerField(null=True, blank=True)
    wage_per_hour_to = models.IntegerField(null=True, blank=True)
    employment_status = models.CharField(max_length=64, choices=EMPLOYMENT_STATUSES_CHOICES,
                                         default=CONTRACT_WITH_NO_PERIOD, null=True, blank=True)
    # working_hours = models.CharField(max_length=64, null=True, blank=True)
    # requirements
    requirements = models.CharField(max_length=9000, null=True, blank=True)
    # benefits
    benefits_description = models.CharField(max_length=9000, null=True, blank=True)
    # company
    company_description = models.CharField(max_length=9000, null=True, blank=True)
    company_name = models.CharField(max_length=128, null=True, blank=True)

    # additional informations
    required_docs = models.CharField(max_length=64, null=True, blank=True)
    clause = models.CharField(max_length=512, null=True, blank=True)
    ref_number = models.CharField(max_length=64, null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
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