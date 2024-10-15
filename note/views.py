# note/views.py
from django.shortcuts import render , redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Note #Dal modulo models.py importo il modello Note
from .forms import NoteForm





# Create your views here.
def note(request):
    note = Note.objects.all().order_by('-id')
     #salvo tutte note all'interno della variabile note e le faccio mandare a schermo in ordine decrescente
    
    return render(request, 'note/test.html' , {"note" : note})  


#INIZIO CREAZIONE CRUD : CREATE
def createNoteView(request):
    
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():#Il metodo is_valid ci aiuta a controllare che tutti i dati definiti nel form, presi dal modello Note sono validi
            form.save()#Nel caso suddetti dati fossero veri vengono salvati nel db
            return redirect("note") #vado a reindirizzare tutto alla vista note. Dopo ver inserito e salvato i dati verrò reindirizzato alla pagina principale note. Si utilizza questa pratica per far si che non vengano spediti da parte dell'utente più volte gli stessi dati (vedi urls.py)
    else:
        form = NoteForm()
    return render(request, "note/form.html", {"form": form})
#Se l'utente ha iniviato il modolo(se esegue una richiesta di tipo post)
#Si crea un Nuovo NoteForm con tutti i dati POST

def updateNoteView(request , f_id):
    obj = get_object_or_404(Note, id=f_id)

    if request.method == "POST":
        form = NoteForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            return redirect("note") 
    else:
        form = NoteForm(instance=obj)
    return render(request ,'note/update.html', {"form":form})



def removeNoteView(request , f_id):
    obj = Note.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("note")
    return render(request, 'note/delete.html', {"obj":obj})