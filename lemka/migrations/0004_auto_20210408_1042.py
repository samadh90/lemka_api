# Generated by Django 3.1.2 on 2021-04-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemka', '0003_auto_20210405_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devis',
            name='remarque',
            field=models.TextField(blank=True, default=''),
        ),
    ]