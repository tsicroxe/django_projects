 #  Inside apps/first_app/views.py
from django.shortcuts import render, HttpResponse
  # While Django will automatically create the request object for us that's passed into our method, HttpResponse objects are our responsibility to create and return to the browser.
  #  Note that 'render' is a shortcut method that combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
  # Create your views here.

  # THIS IS OUR CONTROLLER

def index(request):
  print "*" * 100
  return render(request, "first_app/index.html" )
    # Not using render because we haven't created any templates yet!
