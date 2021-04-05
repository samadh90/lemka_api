# Generated by Django 3.1.2 on 2021-04-05 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lemka', '0002_auto_20210404_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='prix_u_ht',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='detail',
            name='ref_devis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='lemka.devis'),
        ),
    ]
