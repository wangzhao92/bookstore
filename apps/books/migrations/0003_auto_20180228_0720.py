# Generated by Django 2.0.2 on 2018-02-28 07:20

import apps.utils.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180228_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(storage=apps.utils.storage.ImageStorage(), upload_to='books/%Y/%m/', verbose_name='封面'),
        ),
    ]