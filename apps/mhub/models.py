
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z]+$')
# not sure if password regex works, should be greater than 8 characters, contain upper and lower and special character
PASSWORD_REGEX = re.compile(r'^(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$')

class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        inLogin = False

        if 'first_name' not in postData:
            inLogin = True
        if inLogin:
            if not EMAIL_REGEX.match(postData['email_address'].strip().lower()):
                errors["email_address"] = "Invalid email address, please try again."
            if len(postData['password'].strip()) < 8:
                errors["password"] = "Invalid password, please try again."

        if len(errors) == 0:
            currentEmail = postData['email_address'].strip()
            savedUser = User.objects.filter(email_address = currentEmail)
            if not savedUser:
                errors['email_address'] = "That email_address is not registered."
            else:
                passToMatch = bcrypt.checkpw(postData['password'].strip().encode(), savedUser.values()[0]['password'].encode())
                if passToMatch:
                    errors['loginsuccess'] = savedUser

        return errors

    def registration_validator(self, postData):
        errors = {}
        inRegistration = False

        if 'first_name' in postData:
            inRegistration = True
        if inRegistration:
            if len(postData['first_name'].strip()) < 2:
                errors["first_name"] = "First name should be at least 2 characters."
            if len(postData['last_name'].strip()) < 2:
                errors["last_name"] = "Last name should be at least 2 characters."
            if not EMAIL_REGEX.match(postData['email_address'].strip().lower()):
                errors['email_address'] = "Invalid email_address. "
            if len(postData['password'].strip()) < 8:
                errors["password"] = "Password should be at least 8 characters."
            if postData['conf_password'].strip() != postData['password'].strip():
                errors['conf_password'] = "Passwords do not match. "

        if len(errors) == 0:
            currentEmail = postData['email_address']
            if User.objects.filter(email_address = currentEmail):
                errors['email_address'] = "That email_address is already registered, please login."
            else:
                tempHash = bcrypt.hashpw(postData['password'].strip().encode(), bcrypt.gensalt())
                tempUser = User.objects.create(first_name=postData['first_name'].strip(), last_name=postData['last_name'].strip(), email_address=postData['email_address'].strip().lower(), password=tempHash)
                errors['success'] = "Successfully registered. "

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Video(models.Model):
    video_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    saved_by = models.ManyToManyField(User, related_name="saved_videos")