from django.db import models
from main.models import City
from django.contrib.auth.models import User

class Profile(models.Model):
    SelectedCity = models.ForeignKey(City, on_delete=models.SET_DEFAULT, default = 1)
    UserID = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.UserID.username