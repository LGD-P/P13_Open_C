from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    A model representing an address.

    Attributes:
        number (int): The street number of the address.
        street (str): The name of the street.
        city (str): The name of the city.
        state (str): The two-letter abbreviation of the state.
        zip_code (int): The ZIP code of the address.
        country_iso_code (str): The three-letter ISO code of the country.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "Adress"

    def __str__(self):
        """
        A simple string representation of the address in the format "<number> <street>".

        Returns:
            str: The string representation of the address.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    A model representing a letting.

    Attributes:
        title (str): The title of the letting.
        address (Address): The address of the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        A simple string representation of the letting.

        Returns:
            str: The string representation of the letting.
        """
        return self.title
