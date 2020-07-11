from django import forms
from .models import *


class SellForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title' , 'description', 'price', 'author', 'image']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['topic', 'author', 'pdf']
