"""Initialize Flask app."""
from flask import Flask


def init_app():
    """Create Flask application."""
    app = Flask(__name__)

    """
    Create an AppContext. Use as a with block to push the context, which will make current_app point at this application.

    An application context is automatically pushed by RequestContext.push()
    when handling a request, and when running a CLI command. Use this to manually create a context outside of these situations.
    """
    with app.app_context():
        # Import parts of our application
        from .routes import example_blueprint

        # Register Blueprints
        app.register_blueprint(example_blueprint)

        @app.after_request
        def apply_caching(response):
            response.headers["X-Frame-Options"] = "SAMEORIGIN"
            return response

        # app name
        @app.errorhandler(404)
        # inbuilt function which takes error as parameter
        def not_found(e):
            # defining function
            return '404'

        @app.route('/')
        def hello():
            """Return a friendly HTTP greeting."""
            return 'Hello World!'

        return app
