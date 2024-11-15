from flask import Flask
from flask.cli import FlaskGroup
from flask_cors import CORS
from extensions import db, migrate
from routes import bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['WTF_CSRF_ENABLED'] = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "https://supplier-react-frontend.vercel.app"}})

# Initialize the database and migration tool
db.init_app(app)
migrate.init_app(app, db)

# Register the routes blueprint with CORS
app.register_blueprint(bp)

# Set up the CLI commands
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()

