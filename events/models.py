from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class EventHandler(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['event_type'].isalpha()) == False:
            if len(postData['event_type']) < 1:
                errors['event_type'] = "Event Type cannot be empty"

        if (postData['event_name'].isalpha()) == False:
            if len(postData['event_name']) < 1:
                errors['event_name'] = "Event name can not be shorter than 1 characters"

        if (postData['location'].isalpha()) == False:
            if len(postData['location']) < 5:
                errors['location'] = "Location can not be shorter than 5 characters"

        if (postData['cameras_num'] == 0):
            errors['cameras_num'] = "Number of Cameras must be positive."
        
        return errors


class Eventdetails(models.Model):
    event_type = models.CharField(max_length = 255)
    event_name = models.CharField(max_length = 255)
    cameras_num = models.IntegerField(default=0)
    event_id = models.IntegerField(primary_key= True)
    location = models.CharField(max_length = 255)
    objects = EventHandler()



class CameraHandler(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['camera_typ'].isalpha()) == False:
            if len(postData['camera_typ']) < 3:
                errors['camera_typ'] = "Camera type can not be shorter than 3 characters"

        if (postData['cam_location'].isalpha()) == False:
            if len(postData['cam_location']) < 5:
                errors['cam_location'] = "Camera Location can not be shorter than 5 characters"
        return errors


class Cameradetails(models.Model):
    cam_location = models.CharField(max_length = 255)
    cam_event_id = models.IntegerField()
    cam_pid = models.IntegerField(primary_key=True)
    camera_typ = models.CharField(max_length = 255)
    objects = CameraHandler()
