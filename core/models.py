from django.db import models

# SIGNALS
from django.db.models import signals
from django.db.models.signals import pre_save

from django.urls import reverse
# Vão ajudar a botar o nome do produto no link
from django.template.defaultfilters import slugify


class Terminology(models.Model):
    image = models.ImageField('Imagem', upload_to="media/")
    word = models.CharField("Termo", max_length=50)
    AREA = (
        ('Ciências exatas e da terra', 'Ciências exatas e da terra'),
        ('Ciências biológicas', 'Ciências biológicas'),
        ('Engenharias', 'Engenharias'),
        ('Ciências da saúde', 'Ciências da saúde'),
        ('Ciências agrárias', 'Ciências agrárias'),
        ('Ciências sociais e aplicadas', 'Ciências sociais e aplicadas'),
        ('Ciências humanas', 'Ciências humanas'),
        ('Linguística, letras e artes', 'Linguística, letras e artes'),
        ('Outros', 'Outros')
    )
    area = models.CharField("Área", choices=AREA, max_length=30)
    expression = models.CharField("Expressão", max_length=100)
    definition = models.TextField("Definição", max_length=500)
    # Define a data de ciração como sendo a atual
    createdAt = models.DateField('Data de criação', auto_now_add=True)
    updatedAt = models.DateField('Data de atualização', auto_now=True)
    slug = models.SlugField('Slug (adicionado automaticamente)', max_length=100,
                            blank=True)  # O slug do link

    def __str__(self):
        return '%s' % (self.word)


def terminology_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.word)


signals.pre_save.connect(terminology_pre_save, sender=Terminology)
