# Generated by Django 3.0.2 on 2020-07-17 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200716_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminology',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Imagem'),
        ),
    ]
