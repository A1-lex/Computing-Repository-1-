# Generated by Django 5.0.7 on 2025-02-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Computing_Repo', '0007_alter_review_created_at_alter_review_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='review_images/'),
        ),
    ]
