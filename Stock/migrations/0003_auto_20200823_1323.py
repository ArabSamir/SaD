# Generated by Django 3.1 on 2020-08-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0002_auto_20200823_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat',
            name='qte',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vente',
            name='qte',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]