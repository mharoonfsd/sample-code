"""Serializers for the AnApp Django Application."""

from rest_framework import serializers

from AnApp.models import SomeModel


class SomeModelSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for some model."""

    class Meta:
        """Meta attributes for some model serializer."""

        model = SomeModel
        fields = ('col6', 'col7')