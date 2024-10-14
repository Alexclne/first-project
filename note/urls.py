# note/urls.py
from django.urls import path
from .views import note  # Assicurati che questa importazione sia corretta

urlpatterns = [
    path('', note, name='note'),  # Questa è la vista principale per l'app 'note'
]
