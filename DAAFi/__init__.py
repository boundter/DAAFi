import os
from flask import Flask


def create_app(test_config=None):
    """
    Create a flask app with a default configuration.

    This configuration will be overwritten by a config.py file and this should
    be done for proper security. The config files should be located in an
    instance folder in the app directory.
    :param string test_config: The name of the config file for tests in the
                                   instance folder
    :returns: The flask app
    """
    # create the app and an instance folder in the app directory
    app = Flask(__name__, instance_relative_config=True)
    # set a secret key for development and the location of the database
    app.config.from_mapping(
            SECRET_KEY="dev",
            DATABASE=os.path.join(app.instance_path, "DAAFI.sqlite"),
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

    return app
