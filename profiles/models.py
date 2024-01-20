from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This Class defines a Django model for representing a user’s profile.

    Classes:
        - Profile: A model representing a user's profile.

    Attributes:
        - user (User): The User profile.
        - favorite_city (str): The user's favorite city.

    Methods:
        - __str__(): Returns a string representation of the Profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the Profile.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username
