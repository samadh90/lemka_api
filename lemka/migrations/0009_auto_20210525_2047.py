# Generated by Django 3.1.2 on 2021-05-25 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lemka', '0008_auto_20210525_2045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['nom']},
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='nom',
        ),
    ]
