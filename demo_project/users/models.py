from django.db import models

# Create your models here.

class Signup(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    email_address = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    confirm_password = models.CharField(max_length = 50)

    def __str__(self):
        return self.first_name