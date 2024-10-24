# note/views.py
from django.shortcuts import render , redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Note #Dal modulo models.py importo il modello Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def note(request):
    note = Note.objects.all().order_by('-id')
     #salvo tutte note all'interno della variabile note e le faccio mandare a schermo in ordine decrescente
    
    return render(request, 'note/test.html' , {"note" : note})  


#CREATE
@login_required
def create_note_view(request):
    
    if request.method == "POST":#Se l'utente ha iniviato il modolo(se esegue una richiesta di tipo post)
        form = NoteForm(request.POST)#Si crea un Nuovo NoteForm con tutti i dati POST
        if form.is_valid():#Il metodo is_valid ci aiuta a controllare che tutti i dati definiti nel form, presi dal modello Note sono validi
            note = form.save(commit=False)#Creo un'altra istanza che mi permette di non salvare la nota nel database subito
            note.user=request.user #In questo modo associo l'utente che ha creato la nota (request.user) come autore della nota
            note.save()#Nel caso suddetti dati fossero veri vengono salvati nel db
            return redirect("note") #vado a reindirizzare tutto alla vista note. Dopo ver inserito e salvato i dati verrò reindirizzato alla pagina principale note. Si utilizza questa pratica per far si che non vengano spediti da parte dell'utente più volte gli stessi dati (vedi urls.py)
    else:
        form = NoteForm()#Nel caso ci in cui la richiesta fosse ancora get, viene creato un form completamente vuoto
    return render(request, "note/form.html", {"form": form})

@login_required #in questo modo le note potranno essere create solamente da utenti loggati
def note_view( request):
    notes= Note.objects.filter(user=request.user)#In questo modo filtriamo solo le note create dall'user registrato 

    return render( request, 'note/list.html' , {'notes':notes})

#UPDATE
def update_note_view(request , f_id):
    obj = get_object_or_404(Note, id=f_id)
    #Il metodo get_object_or_404 concede di restituire l'oggetto richiesto solo e solamente se esiste. Nel caso l'oggetto non esistesse si genera un errore 404
    if request.method == "POST":
        form = NoteForm(request.POST , instance=obj)
        #All'interno del request.POST si contengono i nuovi dati
        #instance=obj è un argomento che  inica qual'è l'oggetto che si dovrà aggiornare con i nuovi dati.Senza ciò si andrebbe a fare la stessa cosa del metodo Create, andremo a creare un nuovo oggetto
        if form.is_valid():
            form.save()
            return redirect("note") 
    else:
        form = NoteForm(instance=obj)
    return render(request ,'note/update.html', {"form":form})


#DELETE
def remove_note_view(request , f_id):
    obj = Note.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("note")
        
    return render(request, 'note/delete.html', {"obj":obj})

#VIEW FOR AUTH
def registration(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('note')
    else:
        user=UserCreationForm()
    return render(request , "registration/registration.html" , {"user":user})


def new_logout(request):
    print(f"Metodo della richiesta: {request.method}")
    print(f"Contenuto POST: {request.POST}")
    
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('note'))
    else:
        return HttpResponseRedirect(reverse('note'))

