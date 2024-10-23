from django.db import models
from django.contrib.auth.models import User #modello fornito da Django che consente la gestione degli utenti 

# Create your models here.
#CREO E IMPOSTO IN QUESTO CASO DUE PAMETRI DEL MIO MODELLO 'Note'
class Note(models.Model):
    nome = models.CharField(max_length=40)
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add= True)
    utente= models.ForeignKey(User, on_delete=models.CASCADE)#User con questa relazione è il modello figlio. Eseguito import da dja

    def __str__(self):    #In questo modo avremo una rappresentazione esplicita sul Django Administration.Ci verrà ritornato il nome effettivo della nota scritta come titolo
        return self.nome
    

