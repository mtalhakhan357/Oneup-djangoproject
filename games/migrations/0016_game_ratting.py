# Generated by Django 3.1.5 on 2021-04-03 06:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_auto_20210330_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='ratting',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
