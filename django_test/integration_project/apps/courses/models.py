from __future__ import unicode_literals
from django.db import models
from ..login_registration.models import User

class CoursesManager(models.Manager):
    def create(self, **kwargs):
        print "Reached create function in Course manager"
        print kwargs
        new_user = Course(course=kwargs['post']['name'], description=kwargs['post']['description'])
        new_user.save()
        return(True, "Returned")
    def add_user_to_course(self, form_id):
        course = self.get(id=form_id['course'])
        user = User.objects.get(id=form_id['user'])
        course.users.add(user)
        course.save()
        print "User added to course"


class Course(models.Model):
    course = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CoursesManager()
    users = models.ManyToManyField('login_registration.User', related_name = 'courses')
