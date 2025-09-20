from django.db import models
from bases.model import BaseModel

from bases.choices import CabineClass


class Cabine(BaseModel):
    number = models.IntegerField()
    price = models.DecimalField()
    capacity = models.PositiveIntegerField()
    cabine_class = models.Choices(choices=CabineClass.choices)
    description = models.CharField()


class CabineMedia(BaseModel):
    None
