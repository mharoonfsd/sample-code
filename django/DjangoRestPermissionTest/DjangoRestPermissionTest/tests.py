"""Unit tests for DjangoRestPermissionTest."""

import json
from django.core.management import call_command
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory
from rest_framework.viewsets import ModelViewSet
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from AnApp.views import SomeModelViewSet
from AnApp.models import SomeModel
from DjangoRestPermissionTest.permissions import TestRelationModelPermission
from DjangoRestPermissionTest.models import TestModel



class TestRelationModelPermissionTestsOnSomeModelViewSet(TestCase):
    """Test Cases for TestRelationaModelPermission permission class."""

    factory = APIRequestFactory()
    view = SomeModelViewSet()
    permission = TestRelationModelPermission()

    def test_permission_on_list(self):
        """Test TestRelationModelPermission on listing items."""
        users = self.get_users()
        superuser = users.get('superuser')
        staffuser = users.get('staffuser')
        enduser = users.get('enduser')

        request = self.factory.get('/some_models/',
                                   content_type='application/json')

        request.user = superuser 
        self.assertTrue(self.permission.has_permission(request,
                                                       self.view))

        request.user = staffuser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        request.user = enduser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        self.assertIsNotNone(getattr(TestModel,
                                     self.view.item.upper()))

    def test_permission_on_detail(self):
        """Test TestRelationModelPermission on retrueving items."""
        users = self.get_users()
        superuser = users.get('superuser')
        staffuser = users.get('staffuser')
        enduser = users.get('enduser')
        obj = SomeModel.objects.create(col6='hello', col7=15)

        request = self.factory.get('/some_models/{}/'.format(obj.pk),
                                   content_type='application/json')

        request.user = superuser 
        self.assertTrue(self.permission.has_permission(request,
                                                       self.view))

        request.user = staffuser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        request.user = enduser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        self.assertIsNotNone(getattr(TestModel,
                                     self.view.item.upper()))

    def test_permission_on_create(self):
        """Test TestRelationModelPermission on creating items."""
        users = self.get_users()
        superuser = users.get('superuser')
        staffuser = users.get('staffuser')
        enduser = users.get('enduser')

        request = self.factory.post('/some_models/',
                                    json.dumps({'col6': 'hello', 'col7': 15}),
                                    content_type='application/json')

        request.user = superuser 
        self.assertTrue(self.permission.has_permission(request,
                                                       self.view))

        request.user = staffuser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        request.user = enduser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        self.assertIsNotNone(getattr(TestModel,
                                     self.view.item.upper()))

    def test_permission_on_update(self):
        """Test TestRelationModelPermission on updating items."""
        users = self.get_users()
        superuser = users.get('superuser')
        staffuser = users.get('staffuser')
        enduser = users.get('enduser')
        obj = SomeModel.objects.create(col6='hello', col7=15)

        request = self.factory.put('/some_models/{}/'.format(obj.pk),
                                   json.dumps({'col6': 'world', 'col7': 16}),
                                   content_type='application/json')

        request.user = superuser 
        self.assertTrue(self.permission.has_permission(request,
                                                       self.view))

        request.user = staffuser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        request.user = enduser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        self.assertIsNotNone(getattr(TestModel,
                                     self.view.item.upper()))

    def test_permission_on_partial_update(self):
        """Test TestRelationModelPermission on partially updating items."""
        users = self.get_users()
        superuser = users.get('superuser')
        staffuser = users.get('staffuser')
        enduser = users.get('enduser')
        obj = SomeModel.objects.create(col6='hello', col7=15)

        request = self.factory.patch('/some_models/{}/'.format(obj.pk),
                                   json.dumps({'col6': 'world'}),
                                   content_type='application/json')

        request.user = superuser 
        self.assertTrue(self.permission.has_permission(request,
                                                       self.view))

        request.user = staffuser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        request.user = enduser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        self.assertIsNotNone(getattr(TestModel,
                                     self.view.item.upper()))

    def test_permission_on_delete(self):
        """Test TestRelationModelPermission on deleting items."""
        users = self.get_users()
        superuser = users.get('superuser')
        staffuser = users.get('staffuser')
        enduser = users.get('enduser')
        obj = SomeModel.objects.create(col6='hello', col7=15)

        request = self.factory.delete('/some_models/{}/'.format(obj.pk),
                                      json.dumps({'col6': 'world'}),
                                      content_type='application/json')

        request.user = superuser 
        self.assertTrue(self.permission.has_permission(request,
                                                       self.view))

        request.user = staffuser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        request.user = enduser
        self.assertFalse(self.permission.has_permission(request,
                                                        self.view))

        self.assertIsNotNone(getattr(TestModel,
                                     self.view.item.upper()))

    def get_users(self):
        """Return Superuser, staffuser and enduser objects."""
        superuser = User.objects.create_superuser('admin',
                                                  email='superuser@yopmail.com',
                                                  password='hella16p4')
        
        staffuser = User.objects.create_user('barny',
                                             email="staff@djangotest.com",
                                             password="_staffuser123123")
        staffuser.is_staff = True
        staffuser.save()
        
        enduser = User.objects.create_user('john',
                                           email="end@djangotest.com",
                                           password="_endabc123")
                                        
        return {'superuser': superuser,
                'staffuser': staffuser,
                'enduser': enduser}
