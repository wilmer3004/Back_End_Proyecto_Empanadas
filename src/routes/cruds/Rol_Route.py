import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Rol_Service import Rol_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Rol_Model import Rol_Model
from src.security.util.Decorators import require_token

class Rol_Route:
    
    # Deffining the Blueprint for rol routes
    main = Blueprint('rol_blueprint', __name__)
    
    # Route to handle CRUD operations for Rol
    @main.route('/', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_rols():
        try:
            # Call the service to get all rols
            rols = Rol_Service.consult()
            return jsonify(Response_Success("Rols retrieved successfully", rols).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve rols").to_dict()), 500
        
    # Create a new rol
    @main.route('/', methods=['POST'])
    # Route protection with token verification  
    @require_token

    def create_rol():
        try:
            data = request.get_json()
            # Map incoming JSON data to Rol_Model fields
            rol_data = Rol_Model(
                id_rol=None,
                name_rol=data.get('name_rol')  
            )
            rol_data_dict = rol_data.to_dict()
            # Call the service to create a new rol
            result = Rol_Service.create(rol_data_dict)

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Rol created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create rol").to_dict()), 500
    
    # Get a rol by ID
    @main.route('/<int:id>', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_rol_by_id(id):
        try:
            # Call the service to get a rol by ID
            rol = Rol_Service.consult_id(id)
            if rol:
                return jsonify(Response_Success("Rol retrieved successfully", rol).to_dict()), 200
            return jsonify(Response_Error("Rol not found").to_dict()), 404
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve rol").to_dict()), 500
    
    # Update a rol by ID
    @main.route('/<int:id>', methods=['PUT'])
    # Route protection with token verification  
    @require_token

    def update_rol(id):
        try:
            data = request.get_json()
            # Map incoming JSON data to Rol_Model fields
            rol_data = Rol_Model(
                id_rol=id,
                name_rol=data.get('name_rol')  
            )
            # Call the service to update the rol
            result = Rol_Service.update(id, rol_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Rol updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update rol").to_dict()), 500
    
    # Change the state of a rol by ID
    @main.route('/<int:id>/change_state', methods=['PATCH'])
    # Route protection with token verification  
    @require_token

    def change_rol_state(id):
        try:
            # Call the service to change the state of the rol
            result = Rol_Service.change_state(id)

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Rol state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change rol state").to_dict()), 500
        