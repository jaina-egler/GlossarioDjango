# Generated by Django 3.0.2 on 2020-05-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200526_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glossario',
            old_name='defin',
            new_name='definition',
        ),
        migrations.RenameField(
            model_name='glossario',
            old_name='exp',
            new_name='expression',
        ),
        migrations.AddField(
            model_name='glossario',
            name='updatedAt',
            field=models.DateField(auto_now=True, verbose_name='Data de atualização'),
        ),
        migrations.AlterField(
            model_name='glossario',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/', verbose_name='Imagem'),
        ),
    ]
