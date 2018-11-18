# -*- coding: utf-8 -*-
"""Create interface to add data to database."""
from flask import Blueprint, flash, render_template, request, redirect,\
    url_for
from DAAFi.db import get_db

bp = Blueprint("add_data", __name__, url_prefix="/add_data")


def add_entry_name_base(table, formfield, template):
    """Template to add some data to the database.

    This function generates a generic template for adding data consiting only
    of a name to the database.  It checks if the name already exists, and if it
    does an error will be displayed on the webpage.

    Args:
        table (str): The name of the table in the database that should be used.
        formfield (str): The name of the field in the html where the name is
                         given.
        template (str): The name of the html-template.

    Returns:
        flask.render_template: Of the given template.

    """
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
    """Create interface to add the name of associates."""
    return add_entry_name_base("associates", "associates_name",
                               "add_associates.html")


@bp.route("/method", methods=("GET", "POST"))
def add_method():
    """Create interface to add the name of methods."""
    return add_entry_name_base("method", "method_name", "add_method.html")


@bp.route("/category", methods=("GET", "POST"))
def add_category():
    """Create interface to add the name of categories."""
    return add_entry_name_base("category", "category_name",
                               "add_category.html")
