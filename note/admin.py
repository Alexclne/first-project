from django.contrib import admin
#Adesso vado ad inserire i modelli che voglio aggiungere al Database
from .models import Note

# Register your models here.
admin.site.register(Note)