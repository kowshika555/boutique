from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bouquet.db"
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)

# Create Database
with app.app_context():
    db.create_all()

@app.route("/contact", methods=["POST"])
def contact():
    data = request.json
    new_contact = Contact(name=data["name"], email=data["email"], message=data["message"])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"message": "Message saved!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
