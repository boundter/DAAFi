# -*- coding: utf-8 -*-
"""Create interface to add data to database."""
import datetime
from flask import Blueprint, flash, render_template, request, redirect,\
    url_for
from DAAFi.queries import name_in_table, add_name_to_table, get_names,\
    write_transaction

bp = Blueprint("add_data", __name__, url_prefix="/add_data",
               template_folder="templates/add_data")


def add_entry_name_base(table):
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
        flask.render_template: Given template, for the first vist, of if the
                               entry could not succesfully be added.
        flask.redicrect(flask.url_for(Overview.index)): Redirect to the index.

    """
    if request.method == "POST":
        name = request.form["name"]
        error = None

        # check if an entry of the same name already exists
        if not name_in_table(name, table):
            error = "The name {} is already registered.".format(name)

        if error is None:
            add_successful = add_name_to_table(name, table)
            if add_successful:
                return redirect(url_for("Overview.index"))
            else:
                error = "Could not add the new entry."
        flash(error)
    return render_template("add_name.html",
                           table_name=table.replace("_", " ").title())


@bp.route("/contact", methods=("GET", "POST"))
def add_contact():
    """Create interface to add the name of contacts."""
    return add_entry_name_base("contact")


@bp.route("/payment_method", methods=("GET", "POST"))
def add_payment_method():
    """Create interface to add the name of payment_methods."""
    return add_entry_name_base("payment_method")


@bp.route("/category", methods=("GET", "POST"))
def add_category():
    """Create interface to add the name of categories."""
    return add_entry_name_base("category")


@bp.route("/transaction", methods=("GET", "POST"))
def add_transaction():
    """Create interface to add transaction entries.

    Returns:
        flask.render_template: Given template, for the first vist, of if the
                               entry could not succesfully be added.
        flask.redicrect(flask.url_for(Overview.index)): Redirect to the
                                                        index.

    """
    contact = get_names("contact")
    category = get_names("category")
    payment_method = get_names("payment_method")
    today = datetime.datetime.strftime(datetime.date.today(), "%d.%m.%Y")
    if request.method == "POST":
        # these should be correct, since the ids come directly from the db and
        # the values from dropdown
        contact_id = request.form["contact"]
        payment_method_id = request.form["payment_method"]
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
            write_transaction(date, amount, contact_id, payment_method_id,
                              category_id)
            return redirect(url_for("Overview.index"))

    return render_template("add_transaction.html", contact=contact,
                           category=category, payment_method=payment_method,
                           default_date=today)
