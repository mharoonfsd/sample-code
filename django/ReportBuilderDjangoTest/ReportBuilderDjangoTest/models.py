from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """Base model from which all models should Extend from."""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta Information about the Base Model."""
        abstract = True