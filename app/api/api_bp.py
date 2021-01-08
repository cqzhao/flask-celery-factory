from . import api
from ..tasks import db_intensive_operation
from flask import jsonify
from flask import current_app


@api.route('/endpoint')
def some_endpoint():
    print("hello I will schedule a celery background job")
    # with current_app.app_context():
    db_intensive_operation.delay()
    return jsonify({}), 200
