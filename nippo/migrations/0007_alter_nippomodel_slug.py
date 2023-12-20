# Generated by Django 4.2.4 on 2023-11-26 09:22

from django.db import migrations, models
import nippo.models


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0006_nippomodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nippomodel',
            name='slug',
            field=models.SlugField(default=nippo.models.slug_maker, max_length=20, unique=True),
        ),
    ]