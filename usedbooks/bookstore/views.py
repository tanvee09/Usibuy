from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SellForm


def home(request):
    return render(request, 'bookstore/landingpage.html', {'title': 'HOME'})


def buy(request):
    context = {
        'title': 'BUY'
    }
    return render(request, 'bookstore/buy.html', context)


def sell(request):
    return render(request, 'bookstore/sell.html', {'title': 'SELL BOOKS'})


def Book(request):
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('bookstore-home')
    else:
        form = SellForm()

    return render(request, 'bookstore/sell.html', {'form': form})
