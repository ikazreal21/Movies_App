from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from imdb import IMDb

@login_required(login_url='login')
def Home(request):
    ia = IMDb()
    movies = None
    code = None
    images = None
    if request.method == 'POST':
        search = request.POST.get('search')
        movies = ia.search_movie(search)   
        for i in range(len(movies)):
            code = movies[i].movieID
            image = ia.get_movie(code)
            images = image['cover url']

    context = {"movies": movies, "code":code, "images":images}
    return render(request, 'website/home.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username of Password is incorrect")
    return render(request, 'website/login.html')

def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
         form = UserCreationForm()
         if request.method == 'POST':
             form = UserCreationForm(request.POST)
             if form.is_valid():
                 form.save()
                 user = form.cleaned_data.get('username')
                 messages.success(request, "Account Created For " + user)
                 return redirect ('login')
                        
    context = {"forms": form}
    return render(request, 'website/register.html', context)

def Logout(request):
    logout(request)
    return redirect('login')