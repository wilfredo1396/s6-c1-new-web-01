from database.db import db


class messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(1000), nullable=False)

    def _init_(self, firstname, lastname, email, message) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.message = message
        self.email = email

    def _repr_(self) -> str:
        return f"Messages({self.id}, {self.firstname}, '{self.lastname}', '{self.message}' , '{self.email}')"
