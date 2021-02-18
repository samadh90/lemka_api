# Generated by Django 3.1.2 on 2021-02-18 19:58

from django.db import migrations, models
import lemka.utils


class Migration(migrations.Migration):

    dependencies = [
        ('lemka', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_slug',
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=lemka.utils.path_and_rename_user_image),
        ),
    ]
