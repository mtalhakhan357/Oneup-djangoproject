# Generated by Django 3.1.5 on 2021-03-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
