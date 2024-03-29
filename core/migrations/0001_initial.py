# Generated by Django 3.0.2 on 2020-05-18 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glossario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, verbose_name='Termo')),
                ('area', models.CharField(choices=[('Ciências exatas e da terra', 'Ciências exatas e da terra'), ('Ciências biológicas', 'Ciências biológicas'), ('Engenharias', 'Engenharias'), ('Ciências da saúde', 'Ciências da saúde'), ('Ciências agrárias', 'Ciências agrárias'), ('Ciências sociais e aplicadas', 'Ciências sociais e aplicadas'), ('Ciências humanas', 'Ciências humanas'), ('Linguística, letras e artes', 'Linguística, letras e artes'), ('Outros', 'Outros')], max_length=30, verbose_name='Área')),
                ('exp', models.CharField(max_length=50, verbose_name='Expressão')),
            ],
        ),
    ]
