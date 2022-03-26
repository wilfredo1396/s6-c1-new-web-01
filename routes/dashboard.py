from flask import Blueprint, render_template
from models.user import messages

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/messages", methods=["GET", "POST"])
def messages():
    messagesList = messages.query.all()
    return render_template("messages.html", messagesList=messagesList)
