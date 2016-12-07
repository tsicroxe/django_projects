from __future__ import unicode_literals
from django.db import models

class CoursesManager(models.Manager):
    def create(self, **kwargs):
        print "Reached create function in Course manager"
        print kwargs
        new_user = Course(course=kwargs['post']['name'], description=kwargs['post']['description'])
        new_user.save()
        return(True, "Returned")

class Course(models.Model):
    course = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CoursesManager()
