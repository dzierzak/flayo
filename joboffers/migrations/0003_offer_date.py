# Generated by Django 2.0.2 on 2018-02-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0002_auto_20180228_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]