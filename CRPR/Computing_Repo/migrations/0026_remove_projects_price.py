# Generated by Django 5.0.7 on 2025-03-08 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Computing_Repo', '0025_remove_projects_pricing_projects_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='price',
        ),
    ]
