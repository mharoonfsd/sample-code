"""models for library app."""

from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """Base object with common properties."""

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta object for the model."""

        abstract = True


class RackModelManager(models.Manager):
    """Manager for getting info about racks."""


class BookModelManager(models.Manager):
    """Manager for getting info about books."""

    def same_rack_count(self, rack):
        """
        Return the count of books.

            param: rack: RackModel
        """
        # get count from db
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""SELECT count(id) FROM app_book
                       WHERE rack_id = {};""".format(rack.id))

        return cursor.fetchone()[0]


class RackModel(BaseModel):
    """The rack object to hold books."""

    name = models.CharField(max_length=45, unique=True)
    can_hold = models.PositiveIntegerField(default=10)

    # set a custom manager with extra methods
    objects = RackModelManager()

    class Meta:
        """Meta object for the model."""

        db_table = "app_rack"
        verbose_name = "Rack"
        verbose_name_plural = "Racks"

    def __str__(self):
        """Update display name of object."""
        return self.name


class BookModel(BaseModel):
    """The book object having title, author and published date."""

    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    published = models.DateTimeField()
    rack = models.ForeignKey(RackModel)

    # set a custom manager with extra methods
    objects = BookModelManager()

    class Meta:
        """Meta object for the model."""

        db_table = "app_book"
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        """Update display name of object."""
        return self.title
