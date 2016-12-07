from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Product

def index(request):
    print "Views/index"
    try:
        context = {'NAMESPACE':Product.objects.all()}
    except:
        context = dict()
    return render(request, 'APPNAME/index.html', context)

# def new(request):
#     print "views/new"
#     return render(request, 'products/new.html')
#
# def create(request):
#     print 'views/create'
#     if request.method == "POST":
#         result = Product.objects.create(post=request.POST)
#         print result[0]
#         print result[1]
#
#     return redirect(reverse('products:index'))
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
