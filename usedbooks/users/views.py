from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
form = UserCreationForm()
class signup_form(forms.Form):
    email = forms.CharField(
            label = "Email",
            max_length = 200,
            required = True,
            )
    password = forms.CharField(
            label = "Password",
            max_length = 100,
            required = True,
            widget = forms.PasswordInput,
            )
    college = forms.CharField(
            label = "College Name",
            max_length = 200,
            required = True,
            )
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : signup_form,
                                                    'd_form': form})
