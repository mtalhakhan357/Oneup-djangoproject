# Generated by Django 3.1.5 on 2021-03-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_contactrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='user_message',
            field=models.TextField(),
        ),
    ]
