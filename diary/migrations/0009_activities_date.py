# Generated by Django 3.1.2 on 2021-04-02 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0008_activities'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
