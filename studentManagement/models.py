from django.db import models


# Create your models here.
class Student(models.Model):
    """
    Classe responsável pelo cadastro de alunos
    """
    name = models.CharField(max_length=50, blank=False, default="0")
    nascimento = models.DateField(max_length=8, blank=False, default="2000-01-01")
    serie = models.CharField(max_length=6, blank=False, default="0")
    cpf = models.CharField(max_length=8, blank=False, default="0")
    matricula = models.CharField(max_length=14, blank=False, default="0")
    cidade = models.CharField(max_length=40, blank=False, default="0")
    endereco = models.CharField(max_length=70, blank=False, default="0")
    telefone = models.CharField(max_length=14, blank=False, default="0")
    
