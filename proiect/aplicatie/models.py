from django.db import models

# Create your models here.


class Transaction(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.country} --> {self.city}'


class BudgetTransaction(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.country} --> {self.city}'


class VenituriModel(models.Model):
    pass


class VenituriRaportModel(models.Model):
    pass
