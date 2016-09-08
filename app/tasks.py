from app import celery, db
from .models import User


@celery.task
def db_intensive_operation():
    print("Celery background job")
    # db operations
    db.session.commit()
    User.query.all()
    print("Celery background job Done!")

