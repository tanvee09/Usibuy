from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponseRedirect
from .forms import SellForm


def home(request):
    return render(request, 'bookstore/landingpage.html', {'title': 'HOME'})


def buy(request):
    return render(request, 'bookstore/buy.html', {'books': Book.objects.all()})


def detail(request, id):
    book_det = Book.objects.get(id=id)
    return render(request, 'bookstore/book_detail.html', {'book_det': book_det})


def sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore-home')
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
