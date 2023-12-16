from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """A model representing Profile

    Attributes:
        user (User) :  The User profile
        favorite_city (str) : The favorite user city

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """A simple string representation of the Profile.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username
