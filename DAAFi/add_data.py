from flask import Blueprint, flash, render_template, request, redirect,\
    url_for
from DAAFi.db import get_db

bp = Blueprint("add_data", __name__, url_prefix="/add_data")


def add_entry_name_base(table, formfield, template):
    # TODO: table should be cleaned for safety
    if request.method == "POST":
        name = request.form[formfield]
        db = get_db()
        error = None

        # check if an entry of the same name already exists
        if db.execute("SELECT id from " + table + " WHERE name = ?",
                      (name, )).fetchone() is not None:
            error = "The name {} is already registered.".format(name)

        if error is None:
            db.execute("INSERT INTO " + table + " (name) VALUES (?)",
                       (name, ))
            db.commit()
            return redirect(url_for("hello"))

        flash(error)
    return render_template(template)


@bp.route("/associates", methods=("GET", "POST"))
def add_associates():
    return add_entry_name_base("associates", "associates_name",
                               "add_associates.html")


@bp.route("/method", methods=("GET", "POST"))
def add_method():
    return add_entry_name_base("method", "method_name", "add_method.html")


@bp.route("/category", methods=("GET", "POST"))
def add_category():
    return add_entry_name_base("category", "category_name",
                               "add_category.html")
