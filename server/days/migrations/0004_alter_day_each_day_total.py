# Generated by Django 4.2.6 on 2024-09-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0003_alter_day_each_day_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='each_day_total',
            field=models.FloatField(default=0.0),
        ),
    ]
