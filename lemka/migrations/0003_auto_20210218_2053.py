# Generated by Django 3.1.2 on 2021-02-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemka', '0002_auto_20210218_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='rayon',
            name='rayon_slug',
        ),
        migrations.RemoveField(
            model_name='section',
            name='section_slug',
        ),
        migrations.RemoveField(
            model_name='typeproduit',
            name='type_produit_slug',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='nom',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
