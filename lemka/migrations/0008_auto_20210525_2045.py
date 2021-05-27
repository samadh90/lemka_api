# Generated by Django 3.1.2 on 2021-05-25 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemka', '0007_auto_20210525_2026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caracteristique',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='couleur',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='rayon',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='typeproduit',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='typeservice',
            options={'ordering': ['nom']},
        ),
        migrations.AlterField(
            model_name='caracteristique',
            name='nom',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='nom',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]