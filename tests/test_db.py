# -*- coding: utf-8 -*-
"""This module contains test for the database connections."""


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
