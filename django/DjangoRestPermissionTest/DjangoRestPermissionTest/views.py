"""Views for the DjangoRestPermissionTest base project."""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from DjangoRestPermissionTest import serializers
from DjangoRestPermissionTest.models import (TestModel,
                                             AnotherTestModel)
from DjangoRestPermissionTest.permissions import TestModelPermission


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class TestModelViewSet(viewsets.ModelViewSet):
    """API endpoint that allows test model to be viewed or edited."""

    permission_classes = (TestModelPermission,)
    queryset = TestModel.objects.all()
    serializer_class = serializers.TestModelSerializer


class AnotherTestModelViewSet(viewsets.ModelViewSet):
    """API endpoint that allows test model to be viewed or edited."""

    permission_classes = ()
    queryset = AnotherTestModel.objects.all()
    serializer_class = serializers.AnotherTestModelSerializer
