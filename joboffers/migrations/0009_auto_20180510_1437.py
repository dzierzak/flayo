# Generated by Django 2.0.2 on 2018-05-10 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0008_auto_20180506_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='benefits_description',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='clause',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='company_description',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='employment_status',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='ref_number',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='required_docs',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='requirements',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='salary_from',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='salary_to',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='wage_per_hour_from',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='wage_per_hour_to',
        ),
    ]
