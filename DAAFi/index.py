# -*- coding: utf-8 -*-
"""Create the overview of the transactions."""
from flask import Blueprint, render_template

bp = Blueprint("Overview", __name__)


@bp.route("/", methods=("GET", "POST"))
def index():
    """Create the index."""
    return render_template("index.html")
