# Generated by Django 3.2.6 on 2021-09-12 04:24
"""clss migration keep module"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """create model of vote and question"""

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='end date'),
        ),
    ]
