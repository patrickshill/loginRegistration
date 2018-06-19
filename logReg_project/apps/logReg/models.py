from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name must be at least 2 characters"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name must be at least 2 characters"
        return errors

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