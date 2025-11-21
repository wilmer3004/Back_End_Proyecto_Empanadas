import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Customer_Service import Customer_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Customer_Model import Customer_Model
from src.security.util.Decorators import require_token

class Customer_Route:
    main = Blueprint('customer_blueprint', __name__)

    # Get all customers
    @main.route('/', methods=['GET'])
    # Route protection with token verification  
    @require_token
    def get_customers():
        try:
            customers = Customer_Service.consult()
            return jsonify(Response_Success("Customers retrieved successfully", customers).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve customers").to_dict()), 500

    # Create a new customer
    @main.route('/', methods=['POST'])
    # Route protection with token verification  
    @require_token
    def create_customer():
        try:
            data = request.get_json()
            customer_data = Customer_Model(
                id_customer=None,
                id_user_fk=data.get('id_user_fk'),
                customer_detail=data.get('customer_detail'),
                state_customer=True
            )
            data_dict = customer_data.to_dict()
            data_dict["id_type_customer_fk"] = data.get('id_type_customer_fk')

            result = Customer_Service.create(data_dict)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Customer created successfully", result).to_dict()), 201
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create customer").to_dict()), 500

    # Get customer by ID
    @main.route('/<int:id>', methods=['GET'])
    # Route protection with token verification  
    @require_token
    def get_customer_by_id(id):
        try:
            customer = Customer_Service.consult_id(id)
            if "error" in customer:
                return jsonify(Response_Error(customer["error"], code=customer.get("code", 500)).to_dict()), customer.get("code", 500)
            return jsonify(Response_Success("Customer retrieved successfully", customer).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve customer").to_dict()), 500

    # Update customer
    @main.route('/<int:id>', methods=['PUT'])
    # Route protection with token verification  
    @require_token
    def update_customer(id):
        try:
            data = request.get_json()
            customer_data = Customer_Model(
                id_customer=id,
                id_user_fk=data.get('id_user_fk'),
                customer_detail=data.get('customer_detail'),
                state_customer=data.get('state_customer', True)
            )
            data_dict = customer_data.to_dict()
            data_dict["id_type_customer_fk"] = data.get('id_type_customer_fk')

            result = Customer_Service.update(id, data_dict)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Customer updated successfully", result).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update customer").to_dict()), 500

    # Change customer state
    @main.route('/<int:id>/state', methods=['PATCH'])
    # Route protection with token verification  
    @require_token
    def change_customer_state(id):
        try:
            result = Customer_Service.change_state(id)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Customer state changed successfully", result).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change customer state").to_dict()), 500
