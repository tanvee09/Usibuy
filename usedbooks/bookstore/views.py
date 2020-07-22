from django.shortcuts import render, redirect,  get_object_or_404
from .models import Book, Note
from django.http import HttpResponseRedirect
from .forms import SellForm, NoteForm, BookSearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector


def base(request) :
    return render(request, 'bookstore/base.html', {'title': 'HOME'})

def home(request):
    return render(request, 'bookstore/landingpage.html', {'title': 'HOME'})


def buy(request):
    context = {}
    query = ""
    if request.GET :
        query = request.GET['q']
        context['query'] = str(query)
    books = book_list(query)
    context['books'] = books
    return render(request, 'bookstore/buy.html', context)


def detail(request, id):
    book_det = Book.objects.get(id=id)
    return render(request, 'bookstore/book_detail.html', {'book_det': book_det})


@login_required
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

@login_required
def update(request, pk, template_name='bookstore/book_form.html'):
    book = get_object_or_404(Book, id=pk)
    form = SellForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('bookstore-home')
    return render(request, template_name, {'form': form})


@login_required
def book_delete(request, pk, template_name='bookstore/book_confirm_delete.html'):
    book= get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('bookstore-home')
    return render(request, template_name, {'object': book})

def user_posts(request):
    logged_in_user = request.user
    logged_in_user_posts = Book.objects.filter(author=logged_in_user)
    return render(request, 'bookstore/user_post_list.html', {'books': logged_in_user_posts})



def note_list(request):
    notes = Note.objects.all()
    return render(request,'bookstore/note_list.html',{
        'notes': notes})

def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'bookstore/upload_note.html',{
        'form': form
        })
    
def book_list(query = None):
    queryset = set([])
    queries = query.split(" ")
    for q in queries :
        books = Book.objects.annotate(search=SearchVector('title', 'author', 'description'),).filter(search__icontains=q)
        for book in books :
            queryset.add(book)
    return list(queryset)