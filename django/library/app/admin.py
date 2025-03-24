"""admin panel for library app."""

from django.contrib import admin

from  .models import RackModel, BookModel
from .forms import RackAdminForm, BookAdminForm


class RackAdmin(admin.ModelAdmin):
    """Admin settings for Rack object."""

    form = RackAdminForm
    list_display = ('name', 'added')


class BookAdmin(admin.ModelAdmin):
    """Admin settings for Book object."""

    form = BookAdminForm
    list_display = ('title', 'author', 'published', 'rack', 'added')

# Register your models here.
admin.site.register(RackModel, RackAdmin)
admin.site.register(BookModel, BookAdmin)
