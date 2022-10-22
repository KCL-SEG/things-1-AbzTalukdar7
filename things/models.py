from django.db import models
from django.core.validators import MinValueVaidator
from django.core.validators import MaxValueVaidator

class Thing(models.Model):
    name = models.CharField(
        unique = True,
        max_length = 30,
        blank = False
    )
    description = models.Charfield(
        unique = False,
        blank = True,
        max_length = 120
    )
    quantity = models.Integerfield(
        unique = False,
        validators = [MinValueVaidator(0), MaxValueVaidator(120)]
    )
