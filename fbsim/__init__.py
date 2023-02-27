from flask import Flask
from config import Config
from .models import db as root_db, marsh
from flask_migrate import Migrate
from flask_cors import CORS
from .api.routes import api

app = Flask(__name__)
app.register_blueprint(api)
app.config.from_object(Config)
root_db.init_app(app)
migrate = Migrate(app, root_db)
marsh.init_app(app)
CORS(app)

