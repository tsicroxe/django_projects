from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'gift/index.html')
