# -*- coding: utf-8 -*-
"""
This module contains functions to interact with a database in a flask-App.

They offer the ability to connect, initialize and close a database.
"""
import sqlite3
from flask import current_app, g


def get_db():
    """
    Get the database.

    If no databse is available it will be connected.
    :returns: The database
    """
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["Database"],
                               detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_facotry = sqlite3.Row
    return g.db


def close_db():
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
