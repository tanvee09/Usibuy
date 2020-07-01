from django.shortcuts import render
from .models import Book
from django.http import HttpResponseRedirect
from .forms import SellForm

def home(request):
    return render(request, 'bookstore/landingpage.html', {'title': 'HOME'})


def buy(request):
    return render(request, 'bookstore/buy.html', { 'books': Book.objects.all() })

def detail(request, question_id):
    return render(request, 'bookstore/detail.html', { 'book' : Book.objects.get(pk = question_id) })


def sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('bookstore-home')
    else:
        form = SellForm()

    return render(request, 'bookstore/sell.html', {'form': form})
    # return render(request, 'bookstore/sell.html', {'title': 'SELL BOOKS'})


# def Book(request):
#     if request.method == 'POST':
#         form = SellForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('bookstore-home')
#     else:
#         form = SellForm()

#     return render(request, 'bookstore/sell.html', {'form': form})
