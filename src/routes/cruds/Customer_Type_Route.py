import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Customer_Type_Service import Customer_Type_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Customer_Type_Model import Customer_Type_Model

class Customer_Type_Route:
    # Deffining the Blueprint for customer type routes
    main = Blueprint('customer_type_blueprint', __name__)

    # Route to handle CRUD operations for Customer Type
    @main.route('/', methods=['GET'])
    def get_customer_types():
        try:
            # Call the service to get all customer types
            customer_types = Customer_Type_Service.consult()
            return jsonify(Response_Success("Customer types retrieved successfully", customer_types).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve customer types").to_dict()), 500
        
    # Create a new customer type
    @main.route('/', methods=['POST'])
    def create_customer_type():
        try:
            data = request.get_json()
            # Map incoming JSON data to Customer_Type_Model fields
            customer_type_data = Customer_Type_Model(
                id_customer_type=None,
                name_customer_type=data.get('name_customer_type'),
                detail_customer_type=data.get('detail_customer_type')  
            )
            # Call the service to create a new customer type
            result = Customer_Type_Service.create(customer_type_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Customer type created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create customer type").to_dict()), 500
        
    # Get a customer type by ID
    @main.route('/<int:id>', methods=['GET'])
    def get_customer_type_by_id(id):
        try:
            # Call the service to get a customer type by ID
            customer_type = Customer_Type_Service.consult_id(id)
            if customer_type:
                return jsonify(Response_Success("Customer type retrieved successfully", customer_type).to_dict()), 200
            return jsonify(Response_Error("Customer type not found").to_dict()), 404
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve customer type").to_dict()), 500
        
    # Update a customer type by ID
    @main.route('/<int:id>', methods=['PUT'])
    def update_customer_type(id):
        try:
            data = request.get_json()
            # Map incoming JSON data to Customer_Type_Model fields
            customer_type_data = Customer_Type_Model(
                id_customer_type=id,
                name_customer_type=data.get('name_customer_type'),
                detail_customer_type=data.get('detail_customer_type'),            )
            # Call the service to update the customer type
            result = Customer_Type_Service.update(id, customer_type_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Customer type updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update customer type").to_dict()), 500
        
    # Deactivate a customer type by ID
    @main.route('/<int:id>/state', methods=['PATCH'])
    def change_customer_type_state(id):
        try:
            # Call the service to change the state of the customer type
            result = Customer_Type_Service.change_state(id)

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Customer type state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change customer type state").to_dict()), 500