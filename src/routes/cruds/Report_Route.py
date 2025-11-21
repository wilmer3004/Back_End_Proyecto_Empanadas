import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Report_Service import Report_Service
from src.models.cruds.Report_Model import Report_Model
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.security.util.Decorators import require_token

class Report_Route:
    main = Blueprint('report_blueprint', __name__)

    # Get all reports
    @main.route('/', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_reports():
        try:
            reports = Report_Service.consult()
            return jsonify(Response_Success("Reports retrieved successfully", reports).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve reports").to_dict()), 500

    # Create a new report
    @main.route('/', methods=['POST'])
    # Route protection with token verification  
    @require_token

    def create_report():
        try:
            data = request.get_json()
            report_data = Report_Model(
                id_report=None,
                id_report_type_fk=data.get("id_report_type_fk"),
                id_user_fk=data.get("id_user_fk"),
                date_report=data.get("date_report"),
                detail_report=data.get("detail_report"),
                state_report=True
            )
            result = Report_Service.create(report_data.to_dict())
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Report created successfully", result).to_dict()), 201
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create report").to_dict()), 500

    # Get report by ID
    @main.route('/<int:id>', methods=['GET'])
    # Route protection with token verification  
    @require_token

    def get_report_by_id(id):
        try:
            report = Report_Service.consult_id(id)
            if "error" in report:
                return jsonify(Response_Error(report["error"], code=report.get("code", 500)).to_dict()), report.get("code", 500)
            return jsonify(Response_Success("Report retrieved successfully", report).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve report").to_dict()), 500

    # Update report
    @main.route('/<int:id>', methods=['PUT'])
    # Route protection with token verification  
    @require_token

    def update_report(id):
        try:
            data = request.get_json()
            report_data = Report_Model(
                id_report=id,
                id_report_type_fk=data.get("id_report_type_fk"),
                id_user_fk=data.get("id_user_fk"),
                date_report=data.get("date_report"),
                detail_report=data.get("detail_report"),
                state_report=data.get("state_report")
            )
            result = Report_Service.update(id, report_data.to_dict())
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Report updated successfully", result).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update report").to_dict()), 500

    # Change report state
    @main.route('/<int:id>/state', methods=['PATCH'])
    # Route protection with token verification  
    @require_token

    def change_report_state(id):
        try:
            result = Report_Service.change_state(id)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Report state changed successfully", result).to_dict()), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change report state").to_dict()), 500
