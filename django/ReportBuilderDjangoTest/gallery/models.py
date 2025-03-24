from django.db import models
from ReportBuilderDjangoTest.models import BaseModel

# Create your models here.
class PictureModel(BaseModel):
    """Picture model to store pictures in database."""
    
    name = models.CharField(max_length=45)
    category = models.ForeignKey('CategoryModel', on_delete='CASCADE')

    class Meta:
        """Meta information about the Picture model."""
        db_table = 'gallery_picture'


class CategoryModel(BaseModel):
    """Category model for categorizing pictures."""
    
    name = models.CharField(max_length=45)

    class Meta:
        """Meta information about Category model."""
        db_table = 'gallery_category'