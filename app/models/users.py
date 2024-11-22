import bcrypt
from extensions import mongo

class User:
    @staticmethod
    def create_user(username, email, password):
        try:
            user_collection = mongo.db.users
            
            # Check if email already exists
            if user_collection.find_one({"email": email}):
                return {"error": "Email already exists!"}
            
            # Hash password before saving
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            user = {
                "username": username,
                "email": email,
                "password": hashed_password
            }
            
            # Save new user to database
            user_collection.insert_one(user)
            return {"success": "User created successfully!"}
        except Exception as e:
            print(f"Error creating user: {str(e)}")
            return {"error": "Database error occurred"}
    
    @staticmethod
    def find_by_email(email):
        try:
            return mongo.db.users.find_one({"email": email})
        except Exception as e:
            print(f"Error finding user: {str(e)}")
            return None