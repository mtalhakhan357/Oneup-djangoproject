# Generated by Django 3.1.5 on 2021-03-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_s', '0004_auto_20210310_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='rating',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]