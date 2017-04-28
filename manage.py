from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import app
from extensions import db

migrate = Migrate(app.create_app(), db)
manager = Manager(app.create_app())

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()