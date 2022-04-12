from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Create your views here.

def register(req):
    context = {}
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate(req, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(req, new_user)
            return redirect("landing:home")
    else:
        form = RegisterForm()
    context.update({
        "form": form,
        "title": "Signup",
    })
    return render(req, 'register.html', context)


def login_user(req):

    context = {}
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            user = authenticate(req, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(req, user)
                return redirect("landing:home")
    else:
        form = AuthenticationForm()
    context.update({
        'form': form,
        "title": "Login"
    })
    return render(req, 'login.html', context)

@login_required
def logout_user(req):
    logout(req)

    return redirect("landing:home")