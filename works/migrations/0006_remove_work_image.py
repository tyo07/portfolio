# Generated by Django 3.0.4 on 2020-03-25 08:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('works', '0005_auto_20200325_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='image',
        ),
    ]
