# Generated by Django 4.2.2 on 2023-06-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_app_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]