import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Product_Type_Service import Product_Type_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Product_Type_Model import Product_Type_Model
from src.security.util.Decorators import require_token

class Product_Type_Route:
    
    # Deffining the Blueprint for product type routes
    main = Blueprint('product_type_blueprint', __name__)
    # Route to handle CRUD operations for Product Type
    @main.route('/', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_product_types():
        try:
            # Call the service to get all product types
            product_types = Product_Type_Service.consult()
            return jsonify(Response_Success("Product types retrieved successfully", product_types).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve product types").to_dict()), 500
        
    # Create a new product type
    @main.route('/', methods=['POST'])
    # Route protection with token verification  
    @require_token

    def create_product_type():
        try:
            data = request.get_json()
            # Map incoming JSON data to Product_Type_Model fields
            product_type_data = Product_Type_Model(
                id_product_type=None,
                name_product_type=data.get('name_product_type'),
                detail_product_type=data.get('detail_product_type'),
            )
            # Call the service to create a new product type
            result = Product_Type_Service.create(product_type_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Product type created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create product type").to_dict()), 500
    
    # Get a product type by ID
    @main.route('/<int:id>', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_product_type_by_id(id):
        try:
            # Call the service to get a product type by ID
            product_type = Product_Type_Service.consult_id(id)
            if product_type:
                return jsonify(Response_Success("Product type retrieved successfully", product_type).to_dict()), 200
            return jsonify(Response_Error("Product type not found").to_dict()), 404
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve product type").to_dict()), 500
        
    # Update a product type by ID
    @main.route('/<int:id>', methods=['PUT'])
    # Route protection with token verification  
    @require_token

    def update_product_type(id):
        try:
            data = request.get_json()
            # Map incoming JSON data to Product_Type_Model fields
            product_type_data = Product_Type_Model(
                name_product_type=data.get('name_product_type'),
                detail_product_type=data.get('detail_product_type'),
                )
            # Call the service to update the product type
            result = Product_Type_Service.update(id, product_type_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Product type updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update product type").to_dict()), 500
    
    # Change the state of a product type by ID
    @main.route('/<int:id>/state', methods=['PATCH'])
    # Route protection with token verification  
    @require_token

    def change_product_type_state(id):
        try:
            # Call the service to change the state of the product type
            result = Product_Type_Service.change_state(id)

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Product type state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change product type state").to_dict()), 500