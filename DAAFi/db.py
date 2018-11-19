# -*- coding: utf-8 -*-
"""
This module contains functions to interact with a database in a flask-App.

They offer the ability to connect, initialize and close a database.
"""
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """Get the database.

    If no databse is available it will be connected.
    Returns:
        The connection to the database

    """
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"],
                               detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    """Close the connection to the database."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Create the database."""
    # connect to the database and create the file
    db = get_db()
    # excecute schema.sql to create the database structure
    # caution: schema.sql clears the old structure and removes all entries
    # should the databse already exist
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


# cli function to create a new database
@click.command("init_db")
@with_appcontext
def init_db_command():
    """Clear the current database and create a new one."""
    init_db()
    click.echo("Initialized the database")


def init_app(app):
    """Add the functions to interact with the databse to flask factory."""
    # close the databse when quitting the app
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def check_table_name(table):
    """Check if the table name exists in the database."""
    db = get_db()
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table'"
                        ).fetchall()
    available_tables = []
    for row in tables:
        available_tables.append(row[0])
    return table in available_tables
