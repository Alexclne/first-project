from django.db import models

# Create your models here.
#CREO E IMPOSTO DEI PAMETRI DEL MIO MODELLO DI NOTA
class Note(models.Model):
    nome = models.CharField(max_length=40)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.nome