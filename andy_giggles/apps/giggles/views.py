from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def index(request):
    return render(request, "giggles/index.html")

def contact(request):
    return render(request, "giggles/contact.html")
