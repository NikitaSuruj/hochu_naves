# Generated by Django 3.0.14 on 2022-07-24 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220724_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frm1',
            name='number',
            field=models.CharField(max_length=18, validators=[django.core.validators.MinLengthValidator(10, 'Не менее десяти цифр'), django.core.validators.MaxLengthValidator(18, 'Не более десяти цифр')]),
        ),
    ]
