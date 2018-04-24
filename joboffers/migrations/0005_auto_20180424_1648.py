# Generated by Django 2.0.2 on 2018-04-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0004_auto_20180424_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(blank=True, max_length=9000, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('CONTRACT_WITH_NO_PERIOD', 'Employment contract for an unspecified period'), ('Employment contract for a specified period/fixed term', 'Employment contract for a specified period/fixed term'), ('B2B agreement', 'B2B agreement'), ('Project delivery contract', 'Project delivery contract')], default='CONTRACT_WITH_NO_PERIOD', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='salary_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='salary_to',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='wage_per_hour_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='wage_per_hour_to',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='working_hours',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
