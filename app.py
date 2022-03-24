from flask import Flask
from routes.site import site
from routes.dashboard import dashboard


"Crear instancia"
app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(dashboard)
