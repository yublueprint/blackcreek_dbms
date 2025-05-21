from django.db import models

class Livestock(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name