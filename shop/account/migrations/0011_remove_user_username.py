# Generated by Django 4.1 on 2022-09-01 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_user_first_name_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
