# Generated by Django 4.1 on 2022-08-30 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
