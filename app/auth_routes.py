from flask import Blueprint, request, jsonify
from models.users import User
import bcrypt
import jwt
from datetime import datetime, timedelta
from config import Config

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/signup', methods=['OPTIONS', 'POST'])
def signup():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
        
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')

        if not email or not password or not username:
            return jsonify({"error": "All fields are required"}), 400

        existing_user = User.find_by_email(email)
        if existing_user:
            return jsonify({"error": "Email already registered"}), 400
        
        result = User.create_user(username, email, password)
        if 'error' in result:
            return jsonify(result), 400

        return jsonify({"message": "Signup successful!"}), 201
        
    except Exception as e:
        print(f"Error in signup: {str(e)}")
        return jsonify({"error": "Server error occurred"}), 500

@auth_bp.route('/api/auth/login', methods=['OPTIONS', 'POST'])
def login():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
        
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        user = User.find_by_email(email)
        if not user:
            return jsonify({"error": "Email not found"}), 400

        if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return jsonify({"error": "Invalid password"}), 400

        token = jwt.encode({
            'user_id': str(user['_id']),
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, Config.SECRET_KEY, algorithm='HS256')

        return jsonify({
            "message": "Login successful!",
            "token": token,
            "username": user['username']
        }), 200
        
    except Exception as e:
        print(f"Error in login: {str(e)}")
        return jsonify({"error": "Server error occurred"}), 500