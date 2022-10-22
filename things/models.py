from django.db import models

class Thing(models.Model):
    name = models.CharField()
    description = models.Charfield()
    quantity = models.Integerfield()
