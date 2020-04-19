from django.db import models

# Create your models here.

class Contato(models.Model):

    nome = models.CharField(max_length=100, blank=False, null=False)

    telefone = models.CharField(max_length=9)

    email = models.EmailField()

    data_nascimento = models.DateField()
