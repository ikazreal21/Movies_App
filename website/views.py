from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

import requests


# APIKEY = 'pk_ktvqwjdsbowaoqnrf'
# APIKEY = 'k_8q318v4f'
APIKEY = '1a4cb261'


@login_required(login_url='login')
def Details(request, pk):
    movieSearch = None
    # context = None
    movieSearch = requests.get(
        url='http://www.omdbapi.com/?apikey={}&i={}&plot=full'.format(APIKEY, pk)
    )
    movieSearch = movieSearch.json()
    context = {"movies": movieSearch}
    return render(request, 'website/details.html', context)


@login_required(login_url='login')
def Home(request):
    movieSearch = None
    context = None
    if request.method == 'POST':
        search = request.POST.get('search')
        movieSearch = requests.get(
            url='http://www.omdbapi.com/?apikey={}&s={}'.format(APIKEY, search)
        )

        movieSearch = movieSearch.json()
        if movieSearch['Response'] == 'False':
            return HttpResponse("<h1>Movie Not Found</h1>")

        context = {"movies": []}
        for i in movieSearch["Search"]:
            context['movies'].append(
                {
                    "id": i["imdbID"],
                    "image": i["Poster"],
                    "title": i["Title"],
                    "year": i["Year"],
                }
            )
    return render(request, 'website/home.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
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
                return redirect('login')

    context = {"forms": form}
    return render(request, 'website/register.html', context)


def Logout(request):
    logout(request)
    return redirect('login')
