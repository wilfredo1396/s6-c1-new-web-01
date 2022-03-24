from flask import Blueprint, render_template

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/messages")
def messages():
    return render_template("messages.html")
