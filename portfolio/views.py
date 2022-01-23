from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomeUserCreationForm

def index(request):
    return render(request, 'home.html', context = {})

def register(request):
    if request.method == 'GET':
        context = {
            'form' : CustomeUserCreationForm,
        }
        return render(request, 'registration/register.html', context = context)
    elif request.method == 'POST':
        form = CustomeUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()

            login(request, user)
            return redirect(reverse('index'))