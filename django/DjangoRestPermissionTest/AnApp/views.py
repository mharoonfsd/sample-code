"""Views for the app AnApp."""

from rest_framework import viewsets

from AnApp import serializers
from AnApp.models import SomeModel
from DjangoRestPermissionTest.models import TestModel
from DjangoRestPermissionTest.permissions import TestRelationModelPermission


# Create your views here.

class SomeModelViewSet(viewsets.ModelViewSet):
    """API endpoint that allows test model to be viewed or edited."""

    permission_classes = (TestRelationModelPermission,)
    queryset = SomeModel.objects.all()
    serializer_class = serializers.SomeModelSerializer
    item = TestModel.BAR