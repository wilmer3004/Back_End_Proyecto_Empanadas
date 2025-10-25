import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Product_Service import Product_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Product_Model import Product_Model

class Product_Route:

    main = Blueprint('product_blueprint', __name__)

    # Get all products
    @main.route('/', methods=['GET'])
    def get_products():
        try:
            products = Product_Service.consult()
            return jsonify(Response_Success("Products retrieved successfully", products).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve products").to_dict()), 500

    # Create a new product
    @main.route('/', methods=['POST'])
    def create_product():
        try:
            data = request.get_json()
            product_data = Product_Model(
                id_product=None,
                id_product_type_fk=data.get('id_product_type_fk'),
                name_product=data.get('name_product'),
                price_product=data.get('price_product'),
                stock_product=data.get('stock_product'),
                detail_product=data.get('detail_product'),
                state_product=True
            )
            result = Product_Service.create(product_data.to_dict())
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Product created successfully", result).to_dict()), 201
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create product").to_dict()), 500

    # Get a product by ID
    @main.route('/<int:id>', methods=['GET'])
    def get_product_by_id(id):
        try:
            product = Product_Service.consult_id(id)
            if "error" in product:
                return jsonify(Response_Error(product["error"], code=product.get("code", 500)).to_dict()), product.get("code", 500)
            return jsonify(Response_Success("Product retrieved successfully", product).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve product").to_dict()), 500

    # Update a product
    @main.route('/<int:id>', methods=['PUT'])
    def update_product(id):
        try:
            data = request.get_json()
            product_data = Product_Model(
                id_product=id,
                id_product_type_fk=data.get('id_product_type_fk'),
                name_product=data.get('name_product'),
                price_product=data.get('price_product'),
                stock_product=data.get('stock_product'),
                detail_product=data.get('detail_product'),
                state_product=data.get('state_product', True)
            )
            result = Product_Service.update(id, product_data.to_dict())
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Product updated successfully", result).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update product").to_dict()), 500

    # Change product state
    @main.route('/<int:id>/state', methods=['PATCH'])
    def change_product_state(id):
        try:
            result = Product_Service.change_state(id)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Product state changed successfully", result).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change product state").to_dict()), 500
