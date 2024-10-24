from .models import Note 
from django import forms  


class NoteForm(forms.ModelForm): #In questo modo vado a gestire l'inserimento dei dati

    class Meta:
        model = Note
        fields =['nome' , 'description']

        labels = {
            "nome" : "Nome",
            "description" : "Descrizione",
        }

    
