# Generated by Django 3.1.5 on 2021-03-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_auto_20210329_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_categary',
            field=models.CharField(default='Action Action-Adventure Adventure Simulation Stratergy Sports Puzzle Arcade Casual Shooting Emulators Cards ', max_length=100),
        ),
    ]