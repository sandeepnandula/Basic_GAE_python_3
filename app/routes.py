# https://realpython.com/flask-blueprint/
# https://github.com/hackersandslackers/flask-blueprint-tutorial/tree/master/flask_blueprint_tutorial

from flask import Blueprint

example_blueprint = Blueprint('example_blueprint', __name__)


@example_blueprint.route("/api/v1")
def index():
    return "Response from api routes"
