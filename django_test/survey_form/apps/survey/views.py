from django.shortcuts import render, redirect


def index(request):
    return render(request, 'survey/index.html')

def process(request):

    if request.method == "POST":
        print 'getting to process'
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')

    else:
        print "was not a post request"
        return redirect('/')

def result(request):
    return render(request, 'survey/result.html')
