from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Livestock(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    health_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    yield_estimate = models.FloatField()

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    purchase_date = models.DateField()
    maintenance_due = models.DateField()

    def __str__(self):
        return self.name
