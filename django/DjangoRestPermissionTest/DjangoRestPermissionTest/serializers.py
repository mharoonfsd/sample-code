"""Serializers for the DjangoRestPermissionTest base project."""

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from DjangoRestPermissionTest.models import (TestModel,
                                             AnotherTestModel)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the User model."""

    class Meta:
        """Meta attributes for the User model serializer."""

        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the group model."""

    class Meta:
        """Meta attributes for the Group model serializer."""

        model = Group
        fields = ('url', 'name')


class TestModelSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the test model."""

    class Meta:
        """Meta attributes for the test model serializer."""

        model = TestModel
        fields = ('col1', 'col2')


class AnotherTestModelSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for another test model."""

    class Meta:
        """Meta attributes for another test model serializer."""

        model = AnotherTestModel
        fields = ('col4', 'col5')