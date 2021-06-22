from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app
import os

env=os.environ.get("FLASK_ENV","develop")

app=create_app(env)

manage=Manager(app)
manage.add_command("db",MigrateCommand)
manage.run()



