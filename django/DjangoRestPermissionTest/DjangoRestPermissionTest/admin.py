"""Admin Classes for the DjangoRestPermissionTest admin portal."""

from django.contrib import admin

from DjangoRestPermissionTest.models import TestModel


class TestModelAdmin(admin.ModelAdmin):
    """Test model admin class for Django Admin Portsl."""

    model = TestModel


admin.site.register(TestModel, TestModelAdmin)