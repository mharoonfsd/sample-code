"""Signal handlers for celert tasks."""

from celery.signals import task_success

@task_success.connect(sender='tasks.add')
def say_hello():
    """Say hello on successfully running add."""
    print('Hello World!')
