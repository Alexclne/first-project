# note/views.py
from django.shortcuts import render

# Create your views here.
def note(request):
    return render(request, 'note/test.html')  # Assicurati che il template esista