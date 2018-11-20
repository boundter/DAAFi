# -*- coding: utf-8 -*-
"""Test the interface to add data."""
import pytest
import time
from DAAFi.queries import name_in_table
from DAAFi.db import get_db


@pytest.mark.parametrize("table", ("category", "payment_method", "contact"))
def test_add_names_interface(client, table):
    """Test interface to add names to different tables."""
    response = client.get("/add_data/" + table)
    table_string = (">" + table + "<").replace("_", " ").title()
    assert str.encode(table_string) in response.data


@pytest.mark.parametrize("table, new_name", (
    ("category", "Books"),
    ("payment_method", "Paypal"),
    ("contact", "Thalia")
))
def test_add_names_new_name(client, app, table, new_name):
    """Test for only adding new names."""
    response = client.post("/add_data/" + table, data={"name": new_name})
    with app.app_context():
        # somehow name_in_table does not work
        db = get_db()
        entry = db.execute("SELECT id FROM " + table + " WHERE name = ?",
                           (new_name, )).fetchone()
        assert entry is not None
        # redirect to index after successful entry
        assert b"<a href=\"/\">" in response.data


@pytest.mark.parametrize("table, existing_name", (
    ("category", "Fun"),
    ("payment_method", "Cash"),
    ("contact", "Amazon")
))
def test_add_names_unique(client, table, existing_name):
    """Test for only adding new names."""
    response = client.post("/add_data/" + table, data={"name": existing_name})
    name_string = "name " + existing_name + " is"
    assert str.encode(name_string) in response.data
