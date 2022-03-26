from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.site import site
from routes.dashboard import dashboard

"Crear instancia"
app = Flask(__name__)

app.config.from_object("config.BaseConfig")

app.register_blueprint(site)
app.register_blueprint(dashboard)

SQLAlchemy(app)
