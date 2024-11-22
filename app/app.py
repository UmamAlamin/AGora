from flask import Flask
from flask_cors import CORS
from extensions import mongo
from auth_routes import auth_bp
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(config_class)
    
    # Initialize CORS
    CORS(app, origins=["http://localhost:5173"])
    
    # Initialize MongoDB
    mongo.init_app(app)
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)