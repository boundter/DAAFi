# -*- coding: utf-8 -*-
"""A flask-app to organize and analyse financial dataself.

This program keeps track of financial transactions to give a dynamic overview
of the balance between income and expenditure. Additionally it offers detailed
views for the analysis of these records.

Methods:
    flask init_db: Creates the database

"""
import os
from flask import Flask


def create_app(test_config=None):
    """Create a flask app with a default configuration.

    This configuration will be overwritten by a config.py file and this should
    be done for proper security. The config files should be located in an
    instance folder in the app directory.

    Args:
     test_config (str): The name of the config file for tests in the
                        instance folder
    Returns:
        The flask app
    """
    # create the app and an instance folder in the app directory
    app = Flask(__name__, instance_relative_config=True)
    # set a secret key for development and the location of the database
    app.config.from_mapping(
            SECRET_KEY="dev",
            DATABASE=os.path.join(app.instance_path, "DAAFi.sqlite"),
    )

    if test_config is None:
        # set the config from a seperate file
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load test config
        app.config.from_mapping(test_config)

    # create the instance folder if it does not exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # create a test page
    @app.route("/hello")
    def hello():
        return "Hello World!"

    from . import db
    db.init_app(app)

    from DAAFi import add_data, index
    app.register_blueprint(add_data.bp)
    app.register_blueprint(index.bp)

    return app
