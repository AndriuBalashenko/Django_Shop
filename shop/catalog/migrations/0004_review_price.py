# Generated by Django 4.1 on 2022-09-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='price',
            field=models.CharField(default=1, max_length=5, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]