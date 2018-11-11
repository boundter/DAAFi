from flask import Blueprint, flash, render_template, request, redirect,\
    url_for, g
from DAAFi.db import get_db

bp = Blueprint("add_data", __name__, url_prefix="/add_data")


@bp.route("/associates", methods=("GET", "POST"))
def add_associates():
    if request.method == "POST":
        associates_name = request.form["associates_name"]
        db = get_db()
        error = None

        # check if an entry of the same name already exists
        if db.execute("SELECT id from associates WHERE name = ?",
                      (associates_name, )).fetchone() is not None:
            error = "The name {} is already registered.".format(
                associates_name)

        if error is None:
            db.execute("INSERT INTO associates (name) VALUES (?)",
                       (associates_name, ))
            db.commit()
            return redirect(url_for("hello"))

        flash(error)
    return render_template("add_associates.html")


@bp.route("/method", methods=("GET", "POST"))
def add_method():
    if request.method == "POST":
        method_name = request.form["method_name"]
        db = get_db()
        error = None

        # check if an entry of the same name already exists
        if db.execute("SELECT id from method WHERE name = ?",
                      (method_name, )).fetchone() is not None:
            error = "The name {} is already registered.".format(method_name)

        if error is None:
            db.execute("INSERT INTO method (name) VALUES (?)",
                       (method_name, ))
            db.commit()
            return redirect(url_for("hello"))

        flash(error)
    return render_template("add_method.html")
