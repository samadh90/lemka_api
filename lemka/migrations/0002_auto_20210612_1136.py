# Generated by Django 3.1.12 on 2021-06-12 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lemka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='ref_tva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='lemka.tva'),
        ),
    ]
