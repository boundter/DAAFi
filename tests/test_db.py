# -*- coding: utf-8 -*-
"""This module contains test for the database connections."""
from DAAFi.db import check_table_name


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
    with app.app_context():
        true_names = ["associates", "method", "category", "transfer"]
        false_names = ["foo", "bar", "baz"]
        for name in true_names:
            assert check_table_name(name)
        for name in false_names:
            assert not check_table_name(name)
