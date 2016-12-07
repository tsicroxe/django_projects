from __future__ import unicode_literals
from django.db import models
import re


class UserManager (models.Manager):
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
                'first_name':user.first_name,
                'last_name':user.last_name,
                'email':user.email,
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

    def process(self, **kwargs):
        print "Calling process function"

        user = {
            'first_name':kwargs['post']['first_name'],
            'last_name':kwargs['post']['last_name'],
            'email':kwargs['post']['email'],
            'password':kwargs['post']['password'],
            'password_confirm':kwargs['post']['password_confirm']
        }


        error_list = []

        #First all validations so we don't have to go to db if we don't have to

        #Checks first_name validation
        if len(user['first_name']) > 1:
            print "First name length: check"
        else:
            error_list.append('first_name')

        #Checks last_name validation
        if len(user['last_name']) > 1:
            print "Last name length: check"
        else:
            error_list.append('last_name')


        #Checks to see if len of password is at least 8
        if len(user['password']) > 7:
            print "Password length: check"
        else:
            error_list.append('password_length')


        #Checks to see if passwords match
        if user['password'] == user['password_confirm']:
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
            user = User.objects.get(email=kwargs['post']['email'])
            error_list.append("exists")
            print "exists already"
        except:
            new_user = User(first_name=kwargs['post']['first_name'], last_name=kwargs['post']['last_name'], email=kwargs['post']['email'], password=kwargs['post']['password'])

        #Checks to see if errors was created and if so ejects before query
        if error_list:
            print "Returned errors"
            return (True, error_list)
        else:
            print "No errors!"
            new_user.save()
            return (False, "No errors! Continuing on")


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
