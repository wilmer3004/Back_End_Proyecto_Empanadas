import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Order_Prod_Service import Order_Prod_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Order_Prod_Model import Order_Prod_Model
from src.models.cruds.Order_Product_Model import Order_Product_Model

class Order_Prod_Route:
    
    # Deffining the Blueprint for order product routes
    main = Blueprint('order_prod_blueprint', __name__)
    
    # Route to handle CRUD operations for Order Product
    @main.route('/', methods=['GET'])
    def get_order_products():
        try:
            # Call the service to get all order products
            order_products = Order_Prod_Service.consult()
            return jsonify(Response_Success("Order products retrieved successfully", order_products).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve order products").to_dict()), 500
    
    # Create a new order product
    @main.route('/', methods=['POST'])
    def create_order_product():
        try:
            data = request.get_json()
            # Map incoming JSON data to Order_Prod_Model fields
            order_product_data = Order_Prod_Model(
                id_customer_fk=data.get('id_customer_fk'),
                detail_order=data.get('detail_order'),
                date_order=data.get('date_order'),
                state_order=data.get('state_order')
            )
            products = data['products']  # List of products to be added to the order
            order_product_product = []
            
            for product in products:
                order_product_product = Order_Product_Model(
                    id_product_fk=product.get('id_product_fk'),
                    quantity_product=product.get('quantity_product')
                )
                order_product_product.append(order_product_product.to_dict())
            order_product_data.update({"products": order_product_product})
                
            
            # Call the service to create a new order product
            result = Order_Prod_Service.create(order_product_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Order product created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create order product").to_dict()), 500
    
    # Get an order product by ID
    @main.route('/<int:id>', methods=['GET'])
    def get_order_product_by_id(id):
        try:
            # Call the service to get an order product by ID
            order_product = Order_Prod_Service.consult_id(id)
            if order_product:
                return jsonify(Response_Success("Order product retrieved successfully", order_product).to_dict()), 200
            return jsonify(Response_Error("Order product not found").to_dict()), 404
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve order product").to_dict()), 500
        
    # Update an order product by ID
    @main.route('/<int:id>', methods=['PUT'])
    def update_order_product(id):
        try:
            data = request.get_json()
            # Map incoming JSON data to Order_Prod_Model fields
            order_product_data = Order_Prod_Model(
                id_order_prod=id,
                id_customer_fk=data.get('id_customer_fk'),
                detail_order=data.get('detail_order'),
                date_order=data.get('date_order'),
                state_order=data.get('state_order')
            )
            # Call the service to update the order product
            result = Order_Prod_Service.update(id, order_product_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Order product updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update order product").to_dict()), 500
        
    # Update products of an order product by ID
    @main.route('/<int:id>/products', methods=['PUT'])
    def update_order_product_products(id):
        try:
            data = request.get_json()
            order_product_product = Order_Product_Model(
                id_product_fk=data.get('id_product_fk'),
                quantity_product=data.get('quantity_product')
            )
        
            result = Order_Prod_Service.update_product(id, order_product_product)

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Order product's products updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update order product's products").to_dict()), 500
    
    # Change the state of an order product by ID
    @main.route('/<int:id>/state', methods=['PATCH'])
    def change_order_product_state(id):
        try:
            # Call the service to change the state of the order product
            result = Order_Prod_Service.change_state(id)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Order product state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change order product state").to_dict()), 500