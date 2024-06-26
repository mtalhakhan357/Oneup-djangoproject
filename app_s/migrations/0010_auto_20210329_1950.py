# Generated by Django 3.1.5 on 2021-03-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_s', '0009_appcomments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='app_copyright',
            new_name='app_author',
        ),
        migrations.RenameField(
            model_name='app',
            old_name='app_copyright_href',
            new_name='app_author_href',
        ),
        migrations.AddField(
            model_name='app',
            name='page_description',
            field=models.TextField(default='Above 50 Words'),
        ),
        migrations.AlterField(
            model_name='app',
            name='app_tags',
            field=models.TextField(default='"Download (name) for Android for free, without any viruses, from one up , Try the latest version of (name) for Android , name , category , subcategory , etc "'),
        ),
        migrations.AlterField(
            model_name='appcomments',
            name='comment',
            field=models.TextField(),
        ),
    ]
