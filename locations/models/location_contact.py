from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True, null=True)
    webpage = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=2, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.city}'

    def adjust_coordinates(self, coordinates):
        self.latitude = coordinates.latitude
        self.longitude = coordinates.longitude


















