# -*- coding: utf-8 -*-
"""This module contains functions to setup the testing environment."""
import os
import tempfile

import pytest
from DAAFi import create_app
from DAAFi.db import init_db, get_db

# read in SQL for populating test data
with open(os.path.join(os.path.dirname(__file__), "example_data.sql"),
          "rb") as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    """Create flask app for testing with a temporary db."""
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({"TESTING": True, "DATABASE": db_path})

    with app.app_context():
        init_db()

    # create the database and load test data
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    # cleanup temporary files
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """Run the client without server."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Execute cli without server."""
    return app.test_cli_runner()
