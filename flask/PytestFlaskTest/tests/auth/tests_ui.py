"""Tests for auth module."""

from . import client

def get_signin_test():
    """Test signin page."""
    response = client.get('/auth/signin/')
    assert response.status_code == 200