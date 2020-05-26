from django.db import models

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
# Create your models here.
