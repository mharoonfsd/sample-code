"""Proxy Related Views."""
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from proxy.views import proxy_view


@csrf_exempt
def _proxy_view_google(request, *args, **kwargs):
    """Return response from google website."""
    requests_args = {}
    remoteurl = 'https://google.com/'
    return proxy_view(request, remoteurl, requests_args)


@csrf_exempt
def _proxy_view_yahoo(request, *args, **kwargs):
    """Return response from yahoo website."""
    requests_args = {}
    remoteurl = 'https://yahoo.com/'
    return proxy_view(request, remoteurl, requests_args)


@csrf_exempt
def _proxy_view_all(request, *args, **kwargs):
    """Return response from yahoo website."""
    requests_args = {}
    remoteurl = 'http://localhost:5002' + request.path
    print(remoteurl)
    return proxy_view(request, remoteurl, requests_args)


