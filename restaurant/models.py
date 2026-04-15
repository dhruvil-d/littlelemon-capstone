from django.db import models


class Menu(models.Model):
    """Model representing a menu item in the restaurant."""
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    """Model representing a table booking."""
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {str(self.booking_date)}'
