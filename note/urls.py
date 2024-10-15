# note/urls.py
from django.urls import path
from .views import note , createNoteView , updateNoteView # Assicurati che questa importazione sia corretta

urlpatterns = [
    path('', note, name='note'),  # Questa è la vista principale per l'app 'note'
    path('form/' , createNoteView , name= 'create_note'),
    path('update/<int:f_id>/', updateNoteView , name = 'update_note' )
]
