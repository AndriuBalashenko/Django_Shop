# Generated by Django 4.1 on 2022-08-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
    ]
