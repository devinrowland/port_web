# Generated by Django 3.0.9 on 2020-08-05 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20200804_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailentry',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
