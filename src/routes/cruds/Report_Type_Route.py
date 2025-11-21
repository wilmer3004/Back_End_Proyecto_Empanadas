import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Report_Type_Service import Report_Type_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Report_Type_Model import Report_Type_Model
from src.security.util.Decorators import require_token

class Report_Type_Route:
    
    # Deffining the Blueprint for report type routes
    main = Blueprint('report_type_blueprint', __name__)
    
    # Route to handle CRUD operations for Report Type
    @main.route('/', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_report_types():
        try:
            # Call the service to get all report types
            report_types = Report_Type_Service.consult()
            return jsonify(Response_Success("Report types retrieved successfully", report_types).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve report types").to_dict()), 500
        
    # Create a new report type
    @main.route('/', methods=['POST'])
    # Route protection with token verification  
    @require_token

    def create_report_type():
        try:
            data = request.get_json()
            # Map incoming JSON data to Report_Type_Model fields
            report_type_data = Report_Type_Model(
                name_report_type=data.get('name_report_type'),
                detail_report_type=data.get('detail_report_type')  
            )
            # Call the service to create a new report type
            result = Report_Type_Service.create(report_type_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Report type created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create report type").to_dict()), 500
        
    # Get a report type by ID
    @main.route('/<int:id>', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_report_type_by_id(id):
        try:
            # Call the service to get a report type by ID
            report_type = Report_Type_Service.consult_id(id)
            if report_type:
                return jsonify(Response_Success("Report type retrieved successfully", report_type).to_dict()), 200
            return jsonify(Response_Error("Report type not found").to_dict()), 404
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve report type").to_dict()), 500
    
    # Update a report type by ID
    @main.route('/<int:id>', methods=['PUT'])
    # Route protection with token verification  
    @require_token

    def update_report_type(id):
        try:
            data = request.get_json()
            # Call the service to update a report type by ID
            report_type_data = Report_Type_Model(
                name_report_type=data.get('name_report_type'),
                detail_report_type=data.get('detail_report_type')  
            )
            result = Report_Type_Service.update(id, report_type_data)

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Report type updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update report type").to_dict()), 500
    
    # Change the state of a report type by ID
    @main.route('/<int:id>/state', methods=['PATCH'])
    # Route protection with token verification  
    @require_token

    def change_report_type_state(id):
        try:
            # Call the service to change the state of a report type by ID
            result = Report_Type_Service.change_state(id)

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Report type state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change report type state").to_dict()), 500
    
    