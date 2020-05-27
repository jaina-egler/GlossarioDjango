from django.db import models

#SIGNALS
from django.db import signals
from django.template.defaultfilters import slugify #Vão ajudar a botar o nome do produto no link

class Glossario(models.Model):
    image=models.ImageField(upload_to="media/", blank = True)
    word = models.CharField("Termo",max_length=50)
    areaC =(
        ('Ciências exatas e da terra','Ciências exatas e da terra'),
       ( 'Ciências biológicas','Ciências biológicas'),
        ('Engenharias','Engenharias'),
        ('Ciências da saúde','Ciências da saúde'),
        ('Ciências agrárias','Ciências agrárias'),
        ('Ciências sociais e aplicadas','Ciências sociais e aplicadas'),
       ( 'Ciências humanas','Ciências humanas'),
       ( 'Linguística, letras e artes', 'Linguística, letras e artes'),
        ('Outros','Outros')
    )  
    area = models.CharField("Área", choices=areaC, max_length=30)
    exp = models.CharField("Expressão",max_length=50)
    defin = models.TextField("Definição",max_length=150)   
    createdAt = models.DateField('Data de criação', auto_now_add=True)#Define a data de ciração como sendo a atual
    slug = models.SlugField('Slug',max_length=100, blank=True, editable=False)#O slug do link

# Create your models here.
