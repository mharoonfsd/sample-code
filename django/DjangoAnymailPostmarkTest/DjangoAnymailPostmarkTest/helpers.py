"""Helper classes and functions to assist in views."""

from django.core.mail import EmailMessage
from anymail.exceptions import AnymailRequestsAPIError


def anymail_postmark_test():
    """Perform django-anymail with postmark test."""
    message = EmailMessage('Anymail Postmark Test',
                           'Email to test Anymail with Postmark',
                           'usama.ashraf@gsquad.io',
                           ['m.haroon@gsquad.io', 'usama.ashraf@gsquad.io'],
                           [],
                           reply_to=['no-reply@gsquad.io'],
                           headers={'Message-ID': 'foo'},)
    try:
        message.send()
    except AnymailRequestsAPIError as err:
        return str(err)
    return 'Success!'