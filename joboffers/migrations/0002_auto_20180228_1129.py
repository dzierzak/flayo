# Generated by Django 2.0.2 on 2018-02-28 11:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('joboffers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobOffer',
            new_name='Offer',
        ),
    ]