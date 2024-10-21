# note/urls.py
from django.urls import path
from .views import note , create_note_view ,  update_note_view , remove_note_view  , registration #importazione metodi da views.py

urlpatterns = [
    path('', note, name='note'),  # Questa è la vista principale per l'app 'note'
    path('form/' , create_note_view , name= 'create_note'),
    path('update/<int:f_id>/', update_note_view , name = 'update_note' ),
    path('delete/<int:f_id>/', remove_note_view , name = 'remove_note' ),
    #AUTH PATH
    path('registration/', registration , name='registration' ),
]
