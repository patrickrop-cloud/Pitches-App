from logging import Manager
from app import create_app
from app.models import User
from flask_script import Manager,Server

app = create_app('production')

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
if __name__ == '__main__':
    manager.run()


# manager = Manager(app)
# manager.add_command('server',Server)

# if __name__ == '__main__':
#     manager.run()