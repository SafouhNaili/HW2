# Car Showroom API
# This Flask app manages cars in a showroom using a MySQL database.

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="carshowroom-db.cmofp6xgsedl.us-east-1.rds.amazonaws.com",  # Your RDS endpoint
    user="admin",  # RDS username
    password="Password123!",  # RDS password
    database="carshowroom_db"  # database name
)
cursor = db.cursor(dictionary=True)  # Use dictionary=True to get results as dictionaries

# Root route
@app.route('/')
def home():
    return "Welcome to the Car Showroom API! Use /api/carshowroom to interact with the database."

# GET /api/carshowroom - Fetch all cars
@app.route('/api/carshowroom', methods=['GET'])
def get_cars():
    cursor.execute("SELECT * FROM carshowroom")
    result = cursor.fetchall()
    return jsonify(result)

# POST /api/carshowroom - Add a new car
@app.route('/api/carshowroom', methods=['POST'])
def add_car():
    data = request.get_json()
    query = "INSERT INTO carshowroom (carname, carmodel, carcategory, quantity, status) VALUES (%s, %s, %s, %s, %s)"
    values = (data['carname'], data['carmodel'], data['carcategory'], data['quantity'], data['status'])
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "Car added successfully"}), 201

# PUT /api/carshowroom/<id> - Update a car by ID
@app.route('/api/carshowroom/<int:id>', methods=['PUT'])
def update_car(id):
    data = request.get_json()
    query = "UPDATE carshowroom SET carname=%s, carmodel=%s, carcategory=%s, quantity=%s, status=%s WHERE id=%s"
    values = (data['carname'], data['carmodel'], data['carcategory'], data['quantity'], data['status'], id)
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "Car updated successfully"})

# DELETE /api/carshowroom/<id> - Delete a car by ID
@app.route('/api/carshowroom/<int:id>', methods=['DELETE'])
def delete_car(id):
    query = "DELETE FROM carshowroom WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()
    return jsonify({"message": "Car deleted successfully"})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)