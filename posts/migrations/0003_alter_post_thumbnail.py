# Generated by Django 5.0.4 on 2024-11-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='default.png', upload_to='thumbnails'),
        ),
    ]
