# Generated by Django 4.2.5 on 2023-11-12 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_remove_folders_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folders',
            name='Created_At',
        ),
    ]
