from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from bookstore.models import Book, Note
from bookstore.views import search_notes_list, book_list
from django.contrib.auth.decorators import login_required







def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has now been created! You can now log in.')
            return redirect('login')

    elif request.method == 'GET' and 'q' in request.GET and str(request.GET['q']) != "":
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if searchin == 'notes' :
            notes = search_notes_list(query)
            context['notes'] = notes
            return render(request,'bookstore/note_list.html',{'notes': notes})
        else :
            books = book_list(query)
            context['books'] = books
            return render(request, 'bookstore/buy.html', {'books' : books})
    
    else:
        form = UserRegisterForm()
    return render(request,"users/register.html",{'form': form})







@login_required
def profile(request) :
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    
    elif request.method == 'GET' and 'q' in request.GET and str(request.GET['q']) != "":
        context = {}
        query = str(request.GET['q'])
        searchin = str(request.GET['searchin'])
        context['query'] = query
        context['searchin'] = searchin
        if searchin == 'notes' :
            notes = search_notes_list(query)
            context['notes'] = notes
            return render(request,'bookstore/note_list.html',{'notes': notes})
        else :
            books = book_list(query)
            context['books'] = books
            return render(request, 'bookstore/buy.html', {'books' : books})

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {}
    context['u_form'] = u_form
    context['p_form'] = p_form
    context['books'] = Book.objects.filter(author_id=request.user.profile.user_id)
    return render(request, 'users/profile.html', context)