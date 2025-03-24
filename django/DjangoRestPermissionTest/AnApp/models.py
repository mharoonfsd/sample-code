"""Models for the app AnApp."""

from django.db import models

from DjangoRestPermissionTest.models import BaseModel

# Create your models here.


class SomeModel(BaseModel):
    """Some model to test custom permission."""

    col6 = models.CharField(max_length=45)
    col7 = models.PositiveIntegerField()
