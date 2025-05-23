# Generated by Django 5.0.7 on 2025-04-04 13:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Computing_Repo', '0028_delete_flutterwavepayment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IpayPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone', models.CharField(max_length=15)),
                ('status', models.CharField(default='Created', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
