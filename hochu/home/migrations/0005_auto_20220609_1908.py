# Generated by Django 3.0.14 on 2022-06-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_frm2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frm2',
            name='name',
        ),
        migrations.AlterField(
            model_name='frm2',
            name='tip',
            field=models.CharField(choices=[('POLI', 'Поликарбонат'), ('METAL', 'Металлопрофиль'), ('MONO', 'Монолит'), ('SOFT', 'Мягкая кровля'), ('DEREVO', 'Дерево'), ('PROFIL', 'Профильная труба'), ('METCHER', 'Металлочерепица'), ('KOVK', 'Ковка')], default='POLI', max_length=40),
        ),
    ]
