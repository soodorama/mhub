from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z]+$')
# not sure if password regex works, should be greater than 8 characters, contain upper and lower and special character
PASSWORD_REGEX = re.compile(r'^(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$')

class UserManager(models.Manager):
    def register_validator(self,postData):
        errors = {}

        first_name = postData['first_name'].strip()
        last_name = postData['last_name'].strip()
        user_name = first_name + " " + last_name
        email = postData['login_email'].strip().lower()
        password = postData['password'].strip()
        confirm = postData['confirm'].strip()
        

        if len(first_name) < 2 or not NAME_REGEX.match(first_name):
            errors['first_name'] = "Invalid first name: only letters and more than 2 characters"
        if len(last_name) < 2 or not NAME_REGEX.match(last_name):
            errors['last_name'] = "Invalid last name: only letters and more than 2 characters"
        if len(email) < 7 or not EMAIL_REGEX.match(email):
            errors['login_email'] = "Invalid email: must be a valid email"
        if len(password) < 8 or password != confirm:
            errors['password'] = "Invalid password: password must be at least 8 characters and match the confirmation password"
    
        if not errors:
            user = User.objects.filter(email=email)
            if user:
                errors['user'] = "User with that email already exists"
            else:
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                user = User.objects.create(first_name=first_name,last_name=last_name,email=email,password=hashed_pw,level=0)
                errors['success'] = { 
                    'message' : "User successfully registered",
                    'user_id' : user.id,
                    'user_name' : user.user_name
                }

        return errors
    
    def login_validator(self, postData):
        errors = {}

        email = postData['login_email'].strip().lower()
        input_password = postData['login_password'].strip()

        user = User.objects.filter(email=email)
        if not user:
            errors['user'] = "No user with that email"
        else:
            if bcrypt.checkpw(input_password.encode(), user[0].password.encode()):
                errors['success'] = { 
                    'message' : "User successfully logged in",
                    'user_id' : user[0].id,
                    'user_name' : user[0].user_name
                }
            else:
                errors['password'] = "Password incorrect"


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Favorite(models.Model):
    # need to learn ajax for this
    spotify = models.CharField(max_length=255)
    soundcloud = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="favorites")


