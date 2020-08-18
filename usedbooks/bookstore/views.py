from django.shortcuts import render, redirect,  get_object_or_404
from .models import Book, Note, College
from django.http import HttpResponseRedirect
from .forms import SellForm, NoteForm, BookSearchForm, AdvancedBookSearchForm, FilterForm
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector
from users.models import Profile
from django.contrib.auth.models import User


#------------------------------------HOME PAGE-----------------------------------------

def home(request):

    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    return render(request, 'bookstore/landingpage.html', {'title': 'HOME'})





#--------------------------------------BUY PAGE-----------------------------------------

def buy(request):
    
    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    context = {}
    query = ""
    books = book_list(query)
    context['books'] = books
    return render(request, 'bookstore/buy.html', context)





#--------------------------------SHOW DETAILS OF A BOOK-----------------------------------

def detail(request, id):

    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    book_det = Book.objects.get(id=id)
    return render(request, 'bookstore/book_detail.html', {'book_det': book_det})





#-----------------------------FILTER BOOKS BY COLLEGE--------------------------------------

def filter(request):

    if request.GET:
        form = FilterForm(request.GET)
        if form.is_valid():
            colleges = form.cleaned_data.get("college")
            if len(colleges) != 0 :
                books = Book.objects.filter(college__in = colleges)
            else :
                books = Book.objects.all()
            return render(request, 'bookstore/buy.html', {'books': books})
    else:
        form = FilterForm()
    return render(request, 'bookstore/filter.html', {'form': form})





#--------------------------------UPLOAD BOOKS FOR SALE------------------------------------

@login_required
def sell(request):

    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.author_id = request.user
            obj.college = request.user.profile.college
            obj.save()
            if len(College.objects.filter(name = request.user.profile.college)) == 0:
                college = College(name = request.user.profile.college)
                college.save()
            return redirect('bookstore-home')
    else:
        form = SellForm()
    return render(request, 'bookstore/sell.html', {'form': form})





#--------------------------------UPDATE DETAILS OF A BOOK LISTED FOR SALE-------------------------------

@login_required
def update(request, pk, template_name='bookstore/book_form.html'):

    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    book = get_object_or_404(Book, id=pk)
    form = SellForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, template_name, {'form': form})





#----------------------------------DELETE A BOOK LISTED FOR SALE-----------------------------------

@login_required
def book_delete(request, pk, template_name='bookstore/book_confirm_delete.html'):
    
    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    book= get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('profile')
    return render(request, template_name, {'object': book})





#-------------------------------SHOW ALL THE BOOKS LISTED BY USER FOR SALE------------------------

@login_required
def user_posts(request):
    
    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    logged_in_user = request.user
    logged_in_user_posts = Book.objects.filter(author=logged_in_user)
    return render(request, 'bookstore/user_post_list.html', {'books': logged_in_user_posts})





#-------------------------------------NOTES AVAILABLE FOR DOWNLOAD-----------------------------------

def note_list(request):

    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    notes = Note.objects.all()
    return render(request,'bookstore/note_list.html', {'notes': notes})





#--------------------------------------------UPLOAD NOTES---------------------------------------------

def upload_note(request):
    
    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'bookstore/upload_note.html', {'form': form})
    




#------------------------RETURNS LIST OF BOOKS FILTERED ON THE BASIS OF SEARCH INPUT----------------------

def book_list(query = None):
    queryset = set([])
    queries = query.split(" ")
    for q in queries :
        books = Book.objects.annotate(search=SearchVector('title', 'author', 'description'),).filter(search__icontains=q)
        for book in books :
            queryset.add(book)
    return list(queryset)





#---------------------------RETURNS LIST OF NOTES FILTERED ON THE BASIS OF SEARCH INPUT--------------------

def search_notes_list(query = None):
    queryset = set([])
    queries = query.split(" ")
    for q in queries :
        notes = Note.objects.annotate(search=SearchVector('topic', 'author'),).filter(search__icontains=q)
        for note in notes :
            queryset.add(note)
    return list(queryset)





#---------------------------------------------LIST OF COMMERCE BOOKS-------------------------------------------

def commercebuy(request):

    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    books = Book.objects.all().filter(stream__icontains='Commerce')
    return render(request, 'bookstore/buy.html', {'books' : books})





#------------------------------------LIST OF HUMANITIES BOOKS---------------------------------------

def humanitiesbuy(request):
    
    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    books = Book.objects.all().filter(stream__icontains='Humanities')
    return render(request, 'bookstore/buy.html', {'books' : books})





#-----------------------------------------LIST OF ENGINEERING BOOKS--------------------------------------------

def engineeringbuy(request):
    
    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    books = Book.objects.all().filter(stream__icontains='Engineering')
    return render(request, 'bookstore/buy.html', {'books' : books})





#-------------------------------------------LIST OF MEDICAL BOOKS-----------------------------------------------

def medicalbuy(request):
    
    if request.GET :
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if query != "" :
            if searchin == 'notes' :
                notes = search_notes_list(query)
                context['notes'] = notes
                return render(request,'bookstore/note_list.html',{'notes': notes})
            else :
                books = book_list(query)
                context['books'] = books
                return render(request, 'bookstore/buy.html', {'books' : books})

    books = Book.objects.all().filter(stream__icontains='Medical')
    return render(request, 'bookstore/buy.html', {'books' : books})

#-------------------------------------------CONTACT SELLER-----------------------------------------------

def contact(request, id):
    user_s = User.objects.get(id=id)
    return render(request, 'bookstore/contact.html',{'user_s' : user_s})
