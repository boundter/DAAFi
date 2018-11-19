# -*- coding: utf-8 -*-
"""Create interface to add data to database."""
import datetime
from flask import Blueprint, flash, render_template, request, redirect,\
    url_for
from DAAFi.db import get_db
from DAAFi.queries import get_names, write_transaction

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
            return redirect(url_for("Overview.index"))

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


@bp.route("/transaction", methods=("GET", "POST"))
def add_transaction():
    """Create interface to add transaction entries."""
    associates = get_names("associates")
    category = get_names("category")
    method = get_names("method")
    today = datetime.datetime.strftime(datetime.date.today(), "%d.%m.%Y")
    if request.method == "POST":
        # these should be correct, since the ids come directly from the db and
        # the values from dropdown
        associate_id = request.form["associates"]
        method_id = request.form["method"]
        category_id = request.form["category"]

        # make sure the amount is valid
        amount = request.form["amount"]
        error_amount = None
        try:
            float(amount)
        except ValueError:
            error_amount = "{} is not a valid amount.".format(amount)
            flash(error_amount)

        # make sure the date is valid
        date = request.form["date"]
        error_date = None
        try:
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            error_date = "{} is not a valid date.".format(date)
            flash(error_date)

        if (error_amount is None and error_date is None):
            write_transaction(date, amount, associate_id, method_id,
                              category_id)
            return redirect(url_for("Overview.index"))

    return render_template("add_transaction.html", associates=associates,
                           category=category, method=method, date=today)
