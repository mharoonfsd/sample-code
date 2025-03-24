"""Base Project module of DjangoCeleryChannelsTest."""

from celery import Celery

# Celery App
celery_app = Celery('DjangoCeleryChannelsTest', backend='redis://localhost', broker='pyamqp://')