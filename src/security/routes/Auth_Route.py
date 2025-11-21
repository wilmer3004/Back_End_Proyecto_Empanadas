from flask import Blueprint, request, jsonify
from src.security.Security import Security
from src.security.service.Auth_Service import Auth_Service
from src.security.model.Auth_Model import Auth_Model

class Auth_Route:
    main = Blueprint("auth_Blueprint", __name__)
    
    @main.route("/login", methods=["POST"])
    def login():
        data = request.json
        data_auth = Auth_Model(None, None, None, data.get("user_name"), data.get("password_user"), None, None).to_dict()
        
        
        if not data_auth["user_name"] or not data_auth["password_user"]:
            return jsonify({"error": "Username and password are required", "code": 400}), 400
        
        auth_response = Auth_Service.login_user(data_auth["user_name"], data_auth["password_user"])
        
        if auth_response != None:
            token = Security.generate_token(auth_response)
            if token:
                auth_response["token_user"] = token
            else:
                return jsonify({"error": "Failed to generate token", "code": 500}), 500
            
        if "error" in auth_response:
            return jsonify(auth_response), auth_response.get("code", 500)
        
        return jsonify(auth_response), 200