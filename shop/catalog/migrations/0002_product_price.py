# Generated by Django 4.1 on 2022-08-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=1, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
