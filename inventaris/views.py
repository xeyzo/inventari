from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login (request):
    return render(request, 'registration/login.html')

def home (request):
    return redirect('http://127.0.0.1:8000/accounts/login/')