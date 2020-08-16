from django import forms
from .models import *

COLLEGES = []

for college in College.objects.all():
    COLLEGES.append((college.name, college.name))

COLLEGES = sorted(COLLEGES)

class SellForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'author', 'image', 'stream']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['topic', 'author', 'pdf']

class BookSearchForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']
        
class AdvancedBookSearchForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['stream']

class FilterForm(forms.Form):
    college = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=COLLEGES,
    )
