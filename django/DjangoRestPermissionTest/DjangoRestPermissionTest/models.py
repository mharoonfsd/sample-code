"""Base models for the DjangoRestPermissionTest base project."""

from django.db import models


class BaseModel(models.Model):
    """Base model with common properties in all models."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta attributes for the Base model."""

        abstract = True


class TestModel(BaseModel):
    """Model to test custom permissions upon."""

    BAR = 'bar'
    WORLD = 'world'

    col1_choices = ((BAR, 'Bar'),
                    (WORLD, 'World'))

    col1 = models.CharField(max_length=45, choices=col1_choices)
    col2 = models.IntegerField()


class TestRelationModel(BaseModel):
    """Relational model to relate Test mdel and Another Test model."""

    test = models.ForeignKey('TestModel')
    another_test = models.ForeignKey('AnotherTestModel')
    col3 = models.CharField(max_length=45)

class AnotherTestModel(BaseModel):
    """Another Test model with M2M relation to Test model."""

    col4 = models.CharField(max_length=45)
    col5 = models.IntegerField()