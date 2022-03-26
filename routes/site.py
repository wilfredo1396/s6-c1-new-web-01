from flask import Blueprint, render_template
from models.user import messages
from Forms.registerform import userform
from database.db import db

site = Blueprint("site", __name__)


@site.route("/", methods=["GET", "POST"])
def home():
    form = userform()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        message = form.message.data
        newmessage = messages(firstname, lastname, email, message)
        db.session.add(newmessage)
        db.session.commit()
    return render_template("home.html", form=form)


@site.route("/messages")
def messagess():
    messagesList = messages.query.all()
    return render_template("messages.html", messagesList=messagesList)
