from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import random

def index(request):

    #Checks to see if request.session['gold'] exists and if it does not, creates it
    try:
        request.session['gold']
    except:
        request.session["gold"] = 0

        #Checks to see if request.session['activities'] exists and if it does not, creates it
    try:
        request.session['activities']
    except:
        request.session['activities'] = []
    print "Why are you here"

        #Renders the html page we will continually redirect to
    return render(request, 'ninja_gold/index.html')

def process(request):
    if request.method == "POST":
        #Defines our buildings and how much each will randomly generate
        buildings = {
            'farm':random.randint(10,20),
            'cave':random.randint(5,10),
            'house':random.randint(2,5),
            'casino':random.randint(-50,50)
            }


        if request.POST['building'] in buildings:
            result = buildings[request.POST['building']]

            #Adds result to total request.session['gold']
            request.session['gold'] = request.session['gold'] + result

            result_log =    {
                            #If result is not greater than 0, color is red. If greater than it is green.
                            'class': ('red','green')[result > 0],

                            #Formats the output into the string that will be appended in the html
                            'activity': "You went to the {} and {} {} gold!".format(request.POST['building'],
                            ('lost','gained')[result > 0], result)
                            }

        #Appends the request.session['activities'] which will be called upon in the html
        request.session['activities'].append(result_log)

    else:
        print "Received something other than POST request and not expecting one"

    return redirect(reverse('ninja_gold:index'))


#This defines reset button which clears all sessions and resets back to initial load
def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect(reverse('ninja_gold:index'))
