from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from routes.site import site
from routes.dashboard import dashboard


"Crear instancia"
app = Flask(__name__)

app.config.from_object("config.BaseConfig")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://root:Vela_124#@localhost:3306/landingdb"

app.register_blueprint(site)
app.register_blueprint(dashboard)

SQLAlchemy(app)
