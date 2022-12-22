# Generated by Django 3.1.5 on 2021-03-28 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_s', '0008_auto_20210326_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='appcomments',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(default='hello')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_s.app')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_s.appcomments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]