# Generated by Django 3.1 on 2020-08-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat',
            name='prix_u',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vente',
            name='prix_u',
            field=models.FloatField(),
        ),
    ]
