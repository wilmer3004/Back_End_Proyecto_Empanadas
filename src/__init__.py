from flask import Flask
from src.routes.cruds.Person_Route import Person_Route
from src.routes.cruds.Document_Type_Route import Document_Type_Route

app = Flask(__name__)

def init_app(config):
    # Load configuration
    app.config.from_object(config)
    
    # Register Blueprints
    # Register the Person_Route blueprint with a URL prefix
    app.register_blueprint(Person_Route.main, url_prefix='/api/v1/persons')
    # Register the Document_Type_Route blueprint with a URL prefix
    app.register_blueprint(Document_Type_Route.main, url_prefix='/api/v1/document_types')
    
    return app