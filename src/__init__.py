from flask import Flask
from src.routes.cruds.Person_Route import Person_Route
from src.routes.cruds.Document_Type_Route import Document_Type_Route
from src.routes.cruds.Customer_Type_Route import Customer_Type_Route
from src.routes.cruds.Report_Type_Route import Report_Type_Route
from src.routes.cruds.Product_Type_Route import Product_Type_Route
from src.routes.cruds.User_Emp_Route import User_Emp_Route
from src.routes.cruds.Product_Route import Product_Route
from src.routes.cruds.Customer_Route import Customer_Route
from src.routes.cruds.Report_Route import Report_Route
from src.routes.cruds.Rol_Route import Rol_Route
from src.routes.cruds.Sale_Route import Sale_Route
from src.routes.cruds.Order_Prod_Route import Order_Prod_Route
from src.security.routes.Auth_Route import Auth_Route

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
    # Register the User_Emp_Route blueprint with a URL prefix
    app.register_blueprint(User_Emp_Route.main, url_prefix='/api/v1/user_emps')
    # Register the Product_Route blueprint with a URL prefix
    app.register_blueprint(Product_Route.main, url_prefix='/api/v1/products')
    # Register the Customer_Route blueprint with a URL prefix
    app.register_blueprint(Customer_Route.main, url_prefix='/api/v1/customers')
    # Register the Report_Route blueprint with a URL prefix
    app.register_blueprint(Report_Route.main, url_prefix='/api/v1/reports')
    # Register the Rol_Route blueprint with a URL prefix
    app.register_blueprint(Rol_Route.main, url_prefix='/api/v1/rols')
    # Register the Sale_Route blueprint with a URL prefix
    app.register_blueprint(Sale_Route.main, url_prefix='/api/v1/sales')
    # Register the Order_Prod_Route blueprint with a URL prefix
    app.register_blueprint(Order_Prod_Route.main, url_prefix='/api/v1/order_prods')
    # Register the Auth_Route blueprint with a URL prefix
    app.register_blueprint(Auth_Route.main, url_prefix='/api/v1/auth')
    
        
    return app