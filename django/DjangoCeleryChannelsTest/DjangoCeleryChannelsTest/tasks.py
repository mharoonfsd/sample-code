"""Tasks to run for DjangoCeleryChannelsTest."""

# from DjangoCeleryChannelsTest import celery_app
from celery import Celery
from celery.signals import task_postrun


app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    """
    Add two numbers.
    
    :param int|float x: A number that should be added to obtain result.
    :param int|float y: A number that should be added to obtain result.

    :rtype: int|float
    :returns: Sum of two numbers.
    """
    return x + y

@task_postrun.connect(sender='tasks.add')
def say_hello(**kwargs):
    """Say hello on successfully running add."""
    print('Hello World!')
