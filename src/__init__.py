from flask import Flask
from src.routes.cruds.Person_Route import Person_Route
from src.routes.cruds.Document_Type_Route import Document_Type_Route
from src.routes.cruds.Customer_Type_Route import Customer_Type_Route
from src.routes.cruds.Report_Type_Route import Report_Type_Route
from src.routes.cruds.Product_Type_Route import Product_Type_Route

app = Flask(__name__)

def init_app(config):
    # Load configuration
    app.config.from_object(config)
    
    # Register Blueprints
    # Register the Person_Route blueprint with a URL prefix
    app.register_blueprint(Person_Route.main, url_prefix='/api/v1/persons')
    # Register the Document_Type_Route blueprint with a URL prefix
    app.register_blueprint(Document_Type_Route.main, url_prefix='/api/v1/document_types')
    # Register the Customer__Type_Route blueprint with a URL prefix
    app.register_blueprint(Customer_Type_Route.main, url_prefix='/api/v1/customer_types') 
    # Register the Report_Type_Route blueprint with a URL prefix
    app.register_blueprint(Report_Type_Route.main, url_prefix='/api/v1/report_types')
    # Register the Product_Type_Route blueprint with a URL prefix
    app.register_blueprint(Product_Type_Route.main, url_prefix='/api/v1/product_types')
    
    return app