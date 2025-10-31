import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Sale_Service import Sale_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Sale_Model import Sale_Model

class Sale_Route:
    
    # Deffining the Blueprint for sale routes
    main = Blueprint('sale_blueprint', __name__)
    # Route to handle CRUD operations for Sale
    @main.route('/', methods=['GET'])
    def get_sales():
        try:
            # Call the service to get all sales
            sales = Sale_Service.consult()
            return jsonify(Response_Success("Sales retrieved successfully", sales).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve sales").to_dict()), 500  
    
    # Create a new sale
    @main.route('/', methods=['POST'])
    def create_sale():
        try:
            data = request.get_json()
            # Map incoming JSON data to Sale_Model fields
            sale_data = Sale_Model(
                id_sale=None,
                id_order_fk=data.get('id_order_fk'),
                date_sale=data.get('date_sale'),
                total_sale=data.get('total_sale'),
                type_sale=data.get('type_sale'),
            )
            # Call the service to create a new sale
            result = Sale_Service.create(sale_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Sale created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create sale").to_dict()), 500
    
    # Get a sale by ID
    @main.route('/<int:id>', methods=['GET'])
    def get_sale_by_id(id):
        try:
            # Call the service to get a sale by ID
            sale = Sale_Service.consult_id(id)
            if sale:
                return jsonify(Response_Success("Sale retrieved successfully", sale).to_dict()), 200
            return jsonify(Response_Error("Sale not found").to_dict()), 404
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve sale").to_dict()), 500
        
    # Update a sale by ID
    @main.route('/<int:id>', methods=['PUT'])
    def update_sale(id):
        try:
            data = request.get_json()
            # Map incoming JSON data to Sale_Model fields
            sale_data = Sale_Model(
                id_sale=id,
                id_order_fk=data.get('id_order_fk'),
                date_sale=data.get('date_sale'),
                total_sale=data.get('total_sale'),
                type_sale=data.get('type_sale'),
            )
            # Call the service to update the sale
            result = Sale_Service.update(id, sale_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Sale updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update sale").to_dict()), 500
        
    # Change the sale status by ID
    @main.route('/<int:id>/state', methods=['PATCH'])
    def change_sale_state(id):
        try:
            # Call the service to change the state of the sale
            result = Sale_Service.change_state(id)

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Sale state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change sale state").to_dict()), 500