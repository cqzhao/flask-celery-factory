from app import celery, db, create_app


app = create_app('default')
app.app_context().push()
