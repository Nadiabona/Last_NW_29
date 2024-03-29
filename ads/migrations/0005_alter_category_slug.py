# Generated by Django 4.1.7 on 2023-03-14 10:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_selection_options_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
