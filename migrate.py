from flask import Flask
from flask_migrate import Migrate, upgrade
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    upgrade()
