# Generated by Django 4.2.2 on 2023-06-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_app_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tasks',
            field=models.IntegerField(default=0),
        ),
    ]