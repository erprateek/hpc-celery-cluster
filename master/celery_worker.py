from celery import Celery
import os

broker = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")

celery = Celery("tasks", broker=broker)

@celery.task
def add(x, y):
    return x + y
