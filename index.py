from app import app
from database.db import db

with app.app_context():
    db.create_all()

if __name__ == "_main_":
    app.run(debug=True)
