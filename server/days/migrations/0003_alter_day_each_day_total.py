# Generated by Django 4.2.6 on 2024-09-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0002_day_each_day_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='each_day_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
