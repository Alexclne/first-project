from django.db import models

# Create your models here.
#CREO E IMPOSTO IN QUESTO CASO DUE PAMETRI DEL MIO MODELLO 'Note'
class Note(models.Model):
    nome = models.CharField(max_length=40)
    description = models.CharField(max_length=2000)

    #In questo modo avremo una rappresentazione esplicita sul Django Administration
    #Ci verrà ritornato il nome effettivo della nota scritta come titolo
    def __str__(self):
        return self.nome