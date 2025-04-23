import pytest

@pytest.fixture(autouse=True, scope="session")
def configure_celery_for_testing():
    from hpc_celery_cluster.main import celery_app
    celery_app.conf.update(
        task_always_eager=True,
        task_eager_propagates=True,
    )
