# -*- coding: utf-8 -*-
"""This module contains test for the database connections."""
import sqlite3
import pytest
from DAAFi.db import check_table_name, get_db


def test_get_close_db(app):
    """Test the opening and closing of the database."""
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e)


def test_init_db_command(runner, monkeypatch):
    """Check if cli init-db calls the init-db function."""
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    # monkeypatch to only check if the function was called
    monkeypatch.setattr("DAAFi.db.init_db", fake_init_db)
    result = runner.invoke(args=["init_db"])
    # Check for successful initialization
    assert "Initialized" in result.output
    assert Recorder.called


def test_check_table_name(app):
    """Test if check_table_name finds all tables."""
    with app.app_context():
        true_names = ["contact", "payment_method", "category",
                      "money_transfer"]
        false_names = ["foo", "bar", "baz"]
        for name in true_names:
            assert check_table_name(name)
        for name in false_names:
            assert not check_table_name(name)
