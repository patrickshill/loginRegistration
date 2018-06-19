from django.db import models
import re

REGEX_EMAIL = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class UserManager(models.Manager):
    def registration_validator(self, postData):
        valid = True
        errors = {
            "first_name"    : [],
            "last_name"     : [],
            "email"         : [],
            "password"      : []
        }
        
        #first and last name validation
        if len(postData["first_name"]) < 2:
            errors["first_name"].append("First name must be at least 2 characters")
            valid = False
        if not postData["first_name"].isalpha():
            errors["first_name"].append("First name can only contain letters")
            valid = False

        if len(postData["last_name"]) < 2:
            errors["last_name"].append("Last name must be at least 2 characters")
            valid = False
        if not postData["last_name"].isalpha():
            errors["last_name"].append("Last name can only contain letters")
            valid = False
            
        #email validation
        if len(postData["email"]) < 1:
            errors["email"].append("No email provided")
            valid = False
        elif not re.match(REGEX_EMAIL,postData["email"]):
            errors["email"].append("Invalid email address")
            valid = False

        #password validation
        if len(postData["password"]) < 8:
            errors["password"].append("Password must contain at least 8 characters")
            valid = False
        elif postData["password"] != postData["password_confirm"]:
            errors["password"].append("Passwords do not match")
            valid = False
        
        if valid == False:
            return errors

        return False

    def login_validator(self,postData):
        valid = True
        errors = {}

        #check if email in database
        if not User.objects.filter(email=postData["email"]).exists():
            valid = False
        else:
            #compare password form data to database
            user = User.objects.get(email=postData["email"])
            if user.password != postData["password"]:
                valid = False
            
        if not valid:
            errors["login"] = "Invalid username or password"
            return errors

        return False

# Create your models here.
class User(models.Model):
    first_name      = models.CharField(max_length = 255)
    last_name       = models.CharField(max_length = 255)
    email           = models.CharField(max_length = 255)
    password        = models.CharField(max_length = 255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __repr__(self):
        return f"<User: First: {self.first_name}, Last: {self.last_name}, Email: {self.email}, PW: {self.password}"