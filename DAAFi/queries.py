# -*- coding: utf-8 -*-
"""Queries to the database."""
from DAAFi.db import get_db, check_table_name
from DAAFi.helpers import list_to_dict


def get_names(table):
    """Get the names from a given table as dict {id: name}."""
    # TODO: test function
    db = get_db()
    if check_table_name(table):
        # TODO: Check if the table has name column
        names = db.execute("SELECT id, name FROM " + table).fetchall()
    else:
        raise ValueError("The table of name {} does not exits").format(table)
    return list_to_dict(names)


def write_transaction(date, amount, associate_id, method_id, category_id):
    """Write a new entry into the transfer table."""
    db = get_db()
    # date is saved as a timestamp from 01.01.1970
    date = int(date.timestamp())
    db.execute("INSERT INTO transfer " +
               "(date, amount, associates_id, method_id, category_id)" +
               "VALUES (?, ?, ?, ?, ?)",
               (date, amount, associate_id, method_id, category_id))
    db.commit()
