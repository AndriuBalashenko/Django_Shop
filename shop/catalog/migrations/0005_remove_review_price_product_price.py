# Generated by Django 4.1 on 2022-09-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_review_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default=1, max_length=5, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
