from flask import Flask
from src.routes.cruds.Person_Route import Person_Route

app = Flask(__name__)

def init_app(config):
    # Load configuration
    app.config.from_object(config)
    
    # Register Blueprints
    # Register the Person_Route blueprint with a URL prefix
    app.register_blueprint(Person_Route.main, url_prefix='/api/v1/persons')
    
    return app