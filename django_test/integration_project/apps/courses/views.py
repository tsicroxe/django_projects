from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.core.urlresolvers import reverse
from ..login_registration.models import User
from django.db.models import Count

def index(request):

    try:
        print "try on index course page"
        context = {'courses':Course.objects.all()}
    #     print "PRint courses below"
    #     for c in courses:
    #         context = {
    #             'course':c.course,
    #             'description':c.description,
    #             'created_at':c.created_at,
    #             'updated_at':c.updated_at
    #             }
    #         print context['course'], context['description']
    #     print context['']
        print "Try successful"
    except:
        context = dict()
        print "Exception successful"

    # for key in context:
    #     print key['course']

    "You have arrived at the Index"
    return render(request, "courses/index.html", context)

def create(request):
    print "Reached create function"

    if request.method == "POST":

        result = Course.objects.create(post=request.POST)


    print result

    return redirect(reverse('courses:index'))

def destroy(request, id):
    print "reached destroy function"
    delete_course = Course.objects.get(id=id)

    if request.method == "GET":
        context = {
            'course':delete_course
            }
        return render(request, 'courses/confirm_destroy.html', context)

    else:
        # delete_course = Course.objects.get(id=id)
        delete_course.delete()
        return redirect(reverse('courses:index'))

def courses_users(request):
    context = {
    # 'courses':Course.objects.all(),
    'users':User.objects.all(),
    'courses':Course.objects.annotate(students=Count('users')),

    }
    return render(request, 'courses/courses_users.html', context)


def add_user(request):
    if request.method == "POST":
        Course.objects.add_user_to_course(request.POST)
        return redirect(reverse('courses:courses_users'))
