from celery import Celery
import os

broker = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")

celery_app: Celery = Celery("tasks", broker=broker, backend=broker)


@celery_app.task(name="celery_worker.add") # type: ignore
def add(x: int, y: int) -> int:
    return x + y

