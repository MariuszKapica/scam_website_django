# Generated by Django 3.2.7 on 2021-09-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_item_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.URLField(default=''),
        ),
    ]
