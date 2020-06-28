from django.shortcuts import render

def home(request):
    return render(request, 'bookstore/landingpage.html', {'title' : 'HOME'})

def buy(request):
    context = {
        'title': 'BUY'
    }
    return render(request, 'bookstore/buy.html', context)

def sell(request):
    return render(request, 'bookstore/sell.html', {'title' : 'SELL BOOKS'})