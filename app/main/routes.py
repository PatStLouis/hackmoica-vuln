from app.main import bp
from flask import current_app as app
from flask import render_template

@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    token = app.config["TOKEN"]
    user = "Paul"
    return render_template("pages/index.jinja", user=user, token=token)