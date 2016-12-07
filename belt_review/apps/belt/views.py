from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, Review, Book

def index(request):
    print "Views/index"
    try:
        context = {'belt':Model.objects.all()}
    except:
        context = dict()
    return render(request, 'belt/index.html', context)

def register(request):
    print "views/register"
    errors = {
        'name':'Name must be at least 2 letters',
        'email':'Not a valid email address',
        'password_length':'Password minimum length: 8',
        'mismatch':'Passwords do not match',
        'email_invalid':'Not a valid email account',
        'exists':'Account email does not exist'
        }

    result = User.objects.register(post=request.POST)
    print result[0]
    print result[1]
    if result[0] is True:
        error_list = result[1][0]
        for key,error in errors.iteritems():
            if key in error_list:
                print key
                messages.error(request, error)
        return redirect(reverse('belt:index'))
    else:
        error = "Registration successful. Please login now"
        messages.error(request, error)
        return redirect(reverse('belt:index'))

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
            return redirect(reverse('belt:books'))

        elif result[0] is True:
            print result[1]
            error_list = result[1][0]
            print error_list
            for key,error in errors.iteritems():
                if key in error_list:
                    print key
                    messages.error(request, error)
            return redirect(reverse('belt:index'))

def books(request):
    print 'views/books'
    print request.method
    rating = Book.objects.all().order_by('-created_at')[:3]
    context = {
        'latest_books':Book.objects.all().order_by('-created_at')[:3],
        'rating':rating
    }
    return render(request, 'belt/books.html', context)

def add(request):
    print 'views/add'
    return render(request, 'belt/add.html')

def logout(request):
    request.session.clear()
    return redirect(reverse('belt:index'))

# def new(request):
#     print "views/new"
#     return render(request, 'products/new.html')
#
def create(request):
    print request.POST

    print 'views/create'
    print request.method
    print request.session['name']
    # user = User.objects.get(id=request.session['id'])
    # result = Book.objects.create(title=request.POST['title'], author=request.POST['author'], users=user)
    # book = Book.objects.get(id=result.id)
    # review = Review.objects.create(review=request.POST['review'], users=user, rating=request.post['rating'])

    user_id = User.objects.get(id=request.session['id'])
    rating = request.POST['rating']
    result = Book.objects.create(title=request.POST['title'], author=request.POST['author'], users=user_id)
    book = Book.objects.get(id=result.id)
    review = Review.objects.create(review=request.POST['review'], rating=rating, users=user_id, books=book)

    return redirect(reverse('belt:books'))
#
# def show(request, id):
#     show_product = Product.objects.get(id=id)
#     context = {
#         'product':show_product
#     }
#     return render(request, 'products/show.html', context)
#
# def edit(request, id):
#     if request.method == 'GET':
#         print 'views/editget'
#         edit_product = Product.objects.get(id=id)
#         context = {
#             'product':edit_product
#         }
#         return render(request, 'products/edit.html', context)
#     else:
#         return redirect(reverse('products:index'))
#
# def update(request, id):
#     if request.method == "GET":
#         print "views/update"
#         print id
#         redirect(reverse('products:index'))
#     else:
#         print 'views/update'
#         result = Product.objects.update(id, post=request.POST)
#         print result[0]
#         print result[1]
#         return redirect(reverse('products:index'))
#
# def destroy(request, id):
#     if request.method == "GET":
#         print "views/destroy/GET"
#         print "If I were to confirm a product destroy it would be a get request"
#         return redirect(reverse('products:index'))
#     else:
#         print 'views/destroy/POST'
#         print "this would confirm it if it were a form"
#         delete_product = Product.objects.get(id=id)
#         delete_product.delete()
#         return redirect(reverse('products:index'))
