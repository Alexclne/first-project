# note/views.py
from django.shortcuts import render , redirect
from .models import Note #Dal modulo models.py importo il modello Note
from .forms import NoteForm





# Create your views here.
def note(request):
    note = Note.objects.all().order_by('-id')
     #salvo tutte note all'interno della variabile note e le faccio mandare a schermo in ordine decrescente
    
    return render(request, 'note/test.html' , {"note" : note})  


#INIZIO CREAZIONE CRUD : CREATE
def createNoteView(request):
    form = NoteForm 
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():#Il metodo is_valid ci aiuta a controllare che tutti i dati definiti nel form, presi dal modello Note sono validi
            form.save()#Nel caso suddetti dati fossero veri vengono salvati nel db
            return redirect("show_url")
    template_name = "note/form.html"
    context = {"form": form}
    return render(request, template_name, context)
#Se l'utente ha iniviato il modolo(quindi esegue una richiesta di tipo post)
#Si crea un Nuovo NoteForm con tutti i dati POST


