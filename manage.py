import os
from app import create_app, db
from flask_script import Manager, Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)
manager.add_command('shell', Shell(make_context=make_shell_context))


@manager.command
def create_db():
    db.create_all()

if __name__ == '__main__':
        manager.run()
