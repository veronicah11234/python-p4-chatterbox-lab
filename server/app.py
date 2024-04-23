# app.py

from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

# Initialize the Flask application with the SQLAlchemy instance
db.init_app(app)

# Create database tables before running tests
with app.app_context():
    db.create_all()

# Define your routes and endpoints...
