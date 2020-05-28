from django.db import models

class Contact(models.Model):
    name = models.CharField('Nome',max_length=50)
    email = models.EmailField('E-mail',max_length=50)#diferente do charfield, checa se o email é valido
    subject = models.CharField('Assunto',max_length=50)
    message = models.TextField('Mensagem',max_length=300)
    sendAt = models.DateTimeField(auto_now_add=True)
# Create your models here.
