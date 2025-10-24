import traceback
from flask import jsonify, request, Blueprint
from src.services.cruds.Route_Service import Route_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Rol_Model import Rol_Model

class Route_Route:
    
    # Defining the Blueprint for route routes
    main = Blueprint('route_blueprint', __name__)
    
    # Route to handle CRUD operations for Route
    @main.route('/', methods=['GET'])
    def get_routes():
        try:
            # Call the service to get all routes
            routes = Route_Service.consult()
            return jsonify(Response_Success("Routes retrieved successfully", routes).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve routes").to_dict()), 500
    
    # Create a new route
    @main.route('/', methods=['POST'])
    def create_route():
        try:
            # extract JSON data from the request
            data = request.get_json()
            # Map incoming JSON data to Route_Model fields
            route_data = Rol_Model(
                id_route=None,
                name_route=data.get('name_route'),
                state_route=data.get('state_route', True)
            )
            # Call the service to create a new route
            result = Route_Service.create(route_data.to_dict())
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Route created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create route").to_dict()), 500 
        
    #Get a route by ID
    @main.route('/<int:id>', methods=['PUT'])
    def update_route(id):
        try:
            # extract JSON data from the request
            data = request.get_json()
            # Call the service to update the route by ID
            result = Route_Service.update(id, data)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Route updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update route").to_dict()), 500
        
        # Change state of a route ( activate/deactivate)    
    @main.route('/<int:id>/state', methods=['PATCH'])
    def change_route_state(id):
        try:
            # Call the service to change the state of the route by ID
            result = Route_Service.change_state(id)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Route state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change route state").to_dict()), 500
        