from . import api
from ..tasks import db_intensive_operation
from flask import jsonify


@api.route('/endpoint')
def some_endpoint():
    print("hello I will schedule a celery background job")
    db_intensive_operation.delay()
    return jsonify({}), 200
