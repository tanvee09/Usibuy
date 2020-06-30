from django import forms


class SellForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    title = forms.CharField(label='Title of the book', max_length=100)
    description = forms.CharField(label='Description of the book', max_length=400)
    author = forms.CharField(label='Author of the book', max_length=100)
    price = forms.IntegerField(label="Price of the book")
    image = forms.ImageField(label="Image of the book")
