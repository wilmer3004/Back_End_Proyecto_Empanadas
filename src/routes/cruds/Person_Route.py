import traceback
from flask import Blueprint, request, jsonify
from src.services.cruds.Person_Service import Person_Service
from src.utils.Response_Error import Response_Error
from src.utils.Response_Success import Response_Success
from src.models.cruds.Person_Model import Person_Model

class Person_Route:
    
    # Defining the Blueprint for person routes
    main = Blueprint('person_blueprint', __name__)
    
    # Route to handle CRUD operations for Person
    @main.route('/', methods=['GET'])
    def get_persons():
        try:
            # Call the service to get all persons
            people = Person_Service.consult()
            return jsonify(Response_Success("Persons retrieved successfully", people).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve persons").to_dict()), 500
      
    # Create a new person 
    @main.route('/', methods=['POST'])
    def create_person():
        try:
            # extract JSON data from the request
            data = request.get_json()
            # Map incoming JSON data to Person_Model fields
            person_data = Person_Model(
                id_person=None,
                id_document_type_fk=data.get('document_type'),
                doc_person=data.get('doc'),
                first_name_person=data.get('first_name'),
                second_name_person=data.get('second_name'),
                first_last_name_person=data.get('first_last_name'),
                second_last_name_person=data.get('second_last_name'),
                email_person=data.get('email'),
                phone_person=data.get('phone'),
                address_person=data.get('address'),
            )
            # Call the service to create a new person
            result = Person_Service.create(person_data.to_dict())
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Person created successfully", result).to_dict()), 201
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to create person").to_dict()), 500
    
    #Get a person by ID 
    @main.route('/<int:id>', methods=['GET'])
    def get_person_by_id(id):
        try:
            # Call the service to get a person by ID
            person = Person_Service.consult_id(id)
            if person:
                return jsonify(Response_Success("Person retrieved successfully", person).to_dict()), 200
            else:
                return jsonify(Response_Error("Person not found", code=404).to_dict()), 404
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to retrieve person").to_dict()), 500
    
    
    # Update a person's details
    @main.route('/<int:id>', methods=['PUT'])
    def update_person(id):
        try:
            # Extract JSON data from the request
            data = request.get_json()
            # Map incoming JSON data to Person_Model fields
            person_data = Person_Model(
                id_person=id,
                id_document_type_fk=data.get('document_type'),
                doc_person=data.get('doc'),
                first_name_person=data.get('first_name'),
                second_name_person=data.get('second_name'),
                first_last_name_person=data.get('first_last_name'),
                second_last_name_person=data.get('second_last_name'),
                email_person=data.get('email'),
                phone_person=data.get('phone'),
                address_person=data.get('address')
            )
            # Call the service to update the person's details
            result = Person_Service.update(id, person_data.to_dict())
            # Check for errors in the result
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Person updated successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to update person").to_dict()), 500
        
    # Change state of a person (e.g., activate/deactivate)
    @main.route('/<int:id>/change_state', methods=['PATCH'])
    def change_person_state(id):
        try:
            # Call the service to change the person's state
            result = Person_Service.change_state(id)
            # Check for errors in the result
            if "error" in result:
                return jsonify(Response_Error(result["error"], code=result.get("code", 500)).to_dict()), result.get("code", 500)
            return jsonify(Response_Success("Person state changed successfully", result).to_dict()), 200
        # Handle exceptions and return an error response
        except Exception as e:
            traceback.print_exc()
            return jsonify(Response_Error("Failed to change person state").to_dict()), 500
    
        
    
    

