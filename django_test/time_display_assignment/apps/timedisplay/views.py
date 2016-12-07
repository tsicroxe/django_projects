
from django.shortcuts import render
import datetime

def index(request):
  print "*" * 100
  print request.method
  context = {
  'somekey' : datetime.datetime.now()
  }
  return render(request, "timedisplay/index.html", context)
