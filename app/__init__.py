from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config.from_object('config.Config')
    db.init_app(app)
    
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
