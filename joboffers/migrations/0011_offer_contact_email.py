# Generated by Django 2.0.2 on 2018-05-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0010_auto_20180510_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='contact_email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]