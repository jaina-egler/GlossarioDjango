# Generated by Django 3.0.2 on 2020-07-01 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200620_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminology',
            name='image',
            field=models.ImageField(height_field=300, upload_to='media/', verbose_name='Imagem', width_field=300),
        ),
    ]
