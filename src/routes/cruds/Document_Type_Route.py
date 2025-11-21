import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Document_Type_Service import Document_Type_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Document_Type_Model import Document_Type_Model
from src.security.util.Decorators import require_token

class Document_Type_Route:

    # Deffining the Blueprint for document type routes
    main = Blueprint('document_type_blueprint', __name__)
    

    # Route to handle CRUD operations for Document Type
    @main.route('/', methods=['GET'])
    # Route protection with token verification  
    @require_token
    def get_document_types():
        try:
            # Call the service to get all document types
            document_types = Document_Type_Service.consult()
            return jsonify(Response_Success("Document types retrieved successfully", document_types).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve document types").to_dict()), 500
      
        
    # Create a new document type
    @main.route('/', methods=['POST'])
    # Route protection with token verification  
    @require_token
    def create_document_type():
        try:
            data = request.get_json()
            # Map incoming JSON data to Document_Type_Model fields
            document_type_data = Document_Type_Model(
                id_document_type=None,
                name_document_type=data.get('name_document_type'),
                acronym_document_type=data.get('acronym_document_type')  
            )
            # Call the service to create a new document type
            result = Document_Type_Service.create(document_type_data.to_dict())

            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Document type created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create document type").to_dict()), 500
        
    # Get a document type by ID
    @main.route('/<int:id>', methods=['GET'])
    # Route protection with token verification  
    @require_token
    def get_document_type_by_id(id):
        try:
            # Call the service to get a document type by ID
            document_type = Document_Type_Service.consult_id(id)
            if document_type:
                return jsonify(Response_Success("Document type retrieved successfully", document_type).to_dict()), 200
            return jsonify(Response_Error("Document type not found").to_dict()), 404
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve document type").to_dict()), 500
        
    # Update a document type by ID
    @main.route('/<int:id>', methods=['PUT'])
    # Route protection with token verification  
    @require_token
    def update_document_type(id):
        try:
            data = request.get_json()
            # Map incoming JSON data to Document_Type_Model fields
            document_type_data = Document_Type_Model(
                id_document_type=id,
                name_document_type=data.get('name_document_type'),
                acronym_document_type=data.get('acronym_document_type'),
            )
            # Call the service to update the document type
            result = Document_Type_Service.update(id, document_type_data.to_dict())
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Document type updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update document type").to_dict()), 500
    
    # Change the state of a document type by ID
    @main.route('/<int:id>/state', methods=['PATCH'])
    # Route protection with token verification  
    @require_token
    def change_document_type_state(id):
        try:
            # Call the service to change the state of the document type
            result = Document_Type_Service.change_state(id)
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Document type state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change document type state").to_dict()), 500


