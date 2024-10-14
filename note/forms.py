from .models import Note 
from django import forms 


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

        labels = {
        "nome" : "Nome",
        "description" : "Descrizione",
        }

    
