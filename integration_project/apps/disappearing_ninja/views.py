from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'ninja/index.html')

def tmnt(request):
    context = {
        'ninja':'tmnt'
    }
    print "Test"
    return render(request, 'ninja/ninja.html', context)


def ninja(request, color):

    turtles = {
        'red':'raphael',
        'blue':'leonardo',
        'orange':'michelangelo',
        'purple':'donatello'
        }

    if color in turtles:
        context = {
            'ninja':turtles[color]
        }

    else:
        context = {
            'ninja':'notapril'
        }

    return render(request, 'ninja/ninja.html', context)
