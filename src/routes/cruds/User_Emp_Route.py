import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.User_Emp_Service import User_Emp_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.User_Emp_Model import User_Emp_Model
from src.security.util.Decorators import require_token

class User_Emp_Route:

    # Defining the Blueprint for user_emp routes
    main = Blueprint('user_emp_blueprint', __name__)

    # Get all user_emps
    @main.route('/', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_user_emps():
        try:
            user_emps = User_Emp_Service.consult()
            return jsonify(Response_Success("User emps retrieved successfully", user_emps).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve user emps").to_dict()), 500

    # Create a new user_emp
    @main.route('/', methods=['POST'])
    # Route protection with token verification  
    @require_token

    def create_user_emp():
        try:
            data = request.get_json()
            # Map incoming JSON data to the model
            user_emp_data = User_Emp_Model(
                id_user=None,
                id_rol_fk=data.get('id_rol_fk'),
                id_person_fk=data.get('id_person_fk'),
                username_user=data.get('username_user'),
                password_user=data.get('password_user'),
                token_user=data.get('token_user'),
                state_user=True
            )
            result = User_Emp_Service.create(user_emp_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("User emp created successfully", result).to_dict()), 201

        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create user emp").to_dict()), 500

    # Get a user_emp by ID
    @main.route('/<int:id>', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_user_emp_by_id(id):
        try:
            user_emp = User_Emp_Service.consult_id(id)
            if not user_emp:
                return jsonify(Response_Error("User emp not found", code=404).to_dict()), 404
            return jsonify(Response_Success("User emp retrieved successfully", user_emp).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve user emp").to_dict()), 500

    # Update a user_emp by ID
    @main.route('/<int:id>', methods=['PUT'])
    # Route protection with token verification  
    @require_token

    def update_user_emp(id):
        try:
            data = request.get_json()
            # Map incoming JSON data to the model
            user_emp_data = User_Emp_Model(
                id_user=id,
                id_rol_fk=data.get('id_rol_fk'),
                id_person_fk=data.get('id_person_fk'),
                username_user=data.get('username_user'),
                password_user=data.get('password_user'),
                token_user=data.get('token_user'),
                state_user=data.get('state_user', True)
            )
            result = User_Emp_Service.update(id, user_emp_data.to_dict())
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("User emp updated successfully", result).to_dict()), 200

        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update user emp").to_dict()), 500

    # Change user_emp state by ID
    @main.route('/<int:id>/state', methods=['PATCH'])
    # Route protection with token verification  
    @require_token

    def change_user_emp_state(id):
        try:
            result = User_Emp_Service.change_state(id)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("User emp state changed successfully", result).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change user emp state").to_dict()), 500

