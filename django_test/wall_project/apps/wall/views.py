from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'wall/index.html')

def post_message(request):
    if request.method == 'POST':
        

        return redirect(reverse('index'))
