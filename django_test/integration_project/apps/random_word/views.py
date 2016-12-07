from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from random_words import RandomWords
from django.core.urlresolvers import reverse

def index(request):
    print 'Index page'
    return render(request, 'random_word/index.html')

def generate(request):
    print "You made it to generate!"
    if request.method == "POST":

        try:
            request.session['count'] = request.session['count'] + 1
        except:
            request.session['count'] = 1

        #Even though the image uses a random string of letters/nums
        #I wanted to try and do a length 14 word so I imported
        #the the module RandomWords and used a loop
        #to loop randomly through the dictionary until I found a 14
        #letter word. Not the most efficient in terms of speed
        #by any means, but still a functional product.

        rw = RandomWords()
        word = rw.random_word()

        while len(word) != 14:
          word = rw.random_word()
          print "searching for a word"

        request.session['random_word'] = word

        return redirect(reverse('random_word:index'))

    else:

        return redirect(reverse('random_word:index'))


def reset(request):

  if request.method == "POST":
    request.session.clear()
    return redirect(reverse('random_word:index'))

  else:
    return redirect(reverse('random_word:index'))
