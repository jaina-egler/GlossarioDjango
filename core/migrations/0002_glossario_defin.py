# Generated by Django 3.0.2 on 2020-05-19 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossario',
            name='defin',
            field=models.TextField(default='---', max_length=150, verbose_name='Definição'),
            preserve_default=False,
        ),
    ]
