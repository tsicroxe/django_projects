from __future__ import unicode_literals
from django.db import models
import re


class UsersManager(models.Manager):
    def login(self, **kwargs):
        print "Calling login function"

        error_list = []

        if len(kwargs['post']['email']) == 0:
            error_list.append('email_blank')
            return (True, error_list)

        try:
            user = User.objects.get(email=kwargs['post']['email'])
            print "Try successful"
        except:
            error_list.append('exist')
            print "Excepted"
            return (True, error_list)

        if user.password == kwargs['post']['password']:
            print "passwords match"
            user = {
                'name':user.name,
                'alias':user.alias,
                'email':user.email,
                'id':user.id
                }

            return(False, user)
        else:
            if len(kwargs['post']['password']) == 0:
                error_list.append('password_blank')
                print "Password blank"
                return (True, error_list)
            else:
                print "Password contains characters"
                error_list.append('mismatch')
                print "REturning True, error_list"
                return(True, error_list)


    def register(self, **kwargs):

        user = {
            'name':kwargs['post']['name'],
            'alias':kwargs['post']['alias'],
            'email':kwargs['post']['email'],
            'password':kwargs['post']['password'],
            'confirm_pw':kwargs['post']['confirm_pw']
        }

        error_list = []

        #Checks to see if len of password is at least 8
        if len(user['password']) > 7:
            print "Password length: check"
        else:
            error_list.append('password_length')


        #Checks to see if passwords match
        if user['password'] == user['confirm_pw']:
            print "Passwords match"
        else:
            error_list.append('mismatch')

        #Uses regex to check if email is valid
        EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
        if EMAIL_REGEX.match(user['email']):
            EMAIL_REGEX.match(user['email'])
            print "Email successfully validated"

        #If not a valid address, flashes that it is not a.. valid address.
        else:
            error_list.append("email_invalid")

        #This checks to see if email already exists in database and if it does not, creates and saves it
        try:
            user = User.objects.get(email=user['email'])
            error_list.append("exists")
            print "exists already"
        except:
            new_user = User(name=user['name'], alias=user['alias'], email=user['email'], password=user['password'])

        #Checks to see if errors was created and if so ejects before query
            if error_list:
                print "Returned errors"
                return (True, error_list)
            else:
                print "No errors!"
                new_user.save()
                return (False, "No errors! Continuing on")

class User(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    users = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    users = models.ForeignKey(User)
    books = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
