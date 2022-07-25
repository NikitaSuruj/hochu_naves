# Generated by Django 3.0.14 on 2022-06-10 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220610_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='newfrm',
            name='name',
            field=models.CharField(default=0, max_length=20, validators=[django.core.validators.MinLengthValidator(2, 'Не менее двух букв')]),
            preserve_default=False,
        ),
    ]