from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    try:
        print "Begin login page index function"
        request.session['first_name']
        print request.session['first_name']
        return render(request, 'login_registration/hub.html')


    except:
        print "Exception"
        return render(request, 'login_registration/index.html')

def hub(request):
    try:
        print "You've reached the hub!"
        request.session['first_name']
        return render(request, 'login_registration/hub.html')
    except:
        return redirect(reverse('login_registration:index'))

def login(request):

    errors = {
        'email_blank':'Email field cannot be blank. Please enter your email',
        'password_blank':'Password field cannot be blank. Please enter your password',
        'mismatch':'Passwords do not match',
        'exist':'Email does not exist'
        }

    if request.method =="POST":

        print "Made it to login process"
        result = User.objects.login(post=request.POST)

        if result[0] is False:
            user = result[1]
            context = dict()
            for key in user:
                request.session[key] = user[key]
                context['key'] = request.session[key]

            print "Redirecting to Wall"
            #NEED TO REDIRECT TO WALL LATER
            return redirect(reverse('login_registration:hub'))

        elif result[0] is True:
            print result[1]
            error_list = result[1][0]
            print error_list
            for key,error in errors.iteritems():
                if key in error_list:
                    print key
                    messages.error(request, error)
            return redirect('/')

        else:
            print "Something broke"
            return redirect(reverse('index'))

def register(request):
    return render(request, 'login_registration/registration.html')

def process(request):

    errors = {
        'first_name':'First name must be at least 2 letters long',
        'last_name':'Last name must be at least 2 letters long',
        'email':'"Not a valid address',
        'password_length':'Password minimum length: 8',
        'mismatch':'Passwords do not match',
        'email_invalid':'Nice try, Nick'
        }

    if request.method == "POST":

        result = User.objects.process(post=request.POST)

        #print messages
        #
        # for key,error in errors.iteritems():
        #     messages.error(request, error)

        if result[0] is True:
            error_list = result[1]
            print error_list
            print "returned error_list"
            for key,error in errors.iteritems():
                if key in error_list:
                    print key
                    messages.error(request, error)
            return redirect(reverse('login_registration:register'))
        elif result[0] is False:
            return redirect(reverse('login_registration:index'))

def reset(request):
    request.session.clear()
    return redirect(reverse('login_registration:index'))
