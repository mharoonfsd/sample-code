"""Views to test django-anymail with postmark."""

from django.http import HttpResponse
from django.shortcuts import redirect

from .helpers import anymail_postmark_test


def form_view(request):
    """Submit form and redirect to test view."""
    return HttpResponse("""
        <!DOCTYPE html>
            <html>
                <head>
                    <title>Title of the document</title>
                </head>
            <body>
                <form action="/test_view/" method="get">
                    <button type="submit">Test</button>
                </form>
            </body>
        </html>
    """)

def test_view(request):
    """Test django-anymail with postmark."""
    result = anymail_postmark_test()
    return HttpResponse("""
        <!DOCTYPE html>
            <html>
                <head>
                    <title>Title of the document</title>
                </head>
            <body>
                <p>{}</p>
            </body>
        </html>
    """.format(result))