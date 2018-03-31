# Generated by Django 2.0.2 on 2018-03-31 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='certificates',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='joboffers.Certificate'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='education_level',
            field=models.CharField(choices=[('Primary education', 'Primary education'), ('Secondary education', 'Secondary education'), ('Higher education', 'Higher education')], max_length=64),
        ),
        migrations.AlterField(
            model_name='offer',
            name='employment_status',
            field=models.CharField(choices=[('CONTRACT_WITH_NO_PERIOD', 'Employment contract for an unspecified period'), ('Employment contract for a specified period/fixed term', 'Employment contract for a specified period/fixed term'), ('B2B agreement', 'B2B agreement'), ('Project delivery contract', 'Project delivery contract')], default='CONTRACT_WITH_NO_PERIOD', max_length=64),
        ),
    ]
