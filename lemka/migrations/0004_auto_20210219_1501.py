# Generated by Django 3.1.2 on 2021-02-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemka', '0003_auto_20210218_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeservice',
            name='type_service',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
