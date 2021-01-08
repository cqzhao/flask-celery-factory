from app import celery, db, create_app
import os
from celery import Celery, Task


app = create_app('default')
app.app_context().push()

def make_celery(app):
    app.config['broker_url'] = 'redis://localhost:6379/0'
    app.config['result_backend'] = 'redis://localhost:6379/0'
    print(f"app.import_name: {app.import_name}")

    celery = Celery(app.import_name, backend=app.config['result_backend'], broker=app.config['broker_url'])
    celery.conf.update(app.config)

    class ContextTask(Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.test_request_context():
                g.in_celery_task = True
                res = self.run(*args, **kwargs)
                return res

    celery.Task = ContextTask
    celery.config_from_object(__name__)
    print(f"in celery_worker __name__ is {__name__}")
    celery.conf.timezone = 'UTC'
    return celery

celery = make_celery(app)