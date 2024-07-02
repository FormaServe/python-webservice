'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

'''

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Function to get a database connection


def get_db_connection():
    conn = sqlite3.connect('./data/chinook.db')
    conn.row_factory = sqlite3.Row  # This allows us to access the columns by name
    return conn

# Endpoint: Get all employees
# http://localhost:5050/employees


@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute a query to retrieve all employees
    cursor.execute(
        "SELECT EmployeeId, LastName, FirstName, Title, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email FROM employees")
    employees = cursor.fetchall()

    # Convert the query result to a list of dictionaries
    employees_list = [dict(employee) for employee in employees]

    conn.close()
    return jsonify(employees_list)

# Endpoint: Get all tracks
# http://localhost:5050/tracks


@app.route('/tracks', methods=['GET'])
def get_tracks():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute a query to retrieve all tracks
    cursor.execute(
        "SELECT TrackId, Name, Composer, Milliseconds, Bytes, UnitPrice FROM tracks")
    tracks = cursor.fetchall()

    # Convert the query result to a list of dictionaries
    tracks_list = [dict(track) for track in tracks]

    conn.close()
    return jsonify(tracks_list)

# Endpoint: Get a specific track by ID
# http://localhost:5050/track/1
# track not found error http://localhost:5050/track/999999999999999999


@app.route('/track/<int:track_id>', methods=['GET'])
def get_track_by_id(track_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute a query to retrieve the track by ID
    cursor.execute(
        "SELECT TrackId, Name, Composer, Milliseconds, Bytes, UnitPrice FROM tracks WHERE TrackId = ?", (track_id,))
    track = cursor.fetchone()

    conn.close()
    if track is None:
        return jsonify({'error': 'Track not found'}), 404

    return jsonify(dict(track))

# Endpoint: Get an individual employee by EmployeeId
# http://localhost:5050/employee/1


@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute a query to retrieve the employee by EmployeeId
    cursor.execute("SELECT EmployeeId, LastName, FirstName, Title, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email FROM employees WHERE EmployeeId = ?", (employee_id,))
    employee = cursor.fetchone()

    conn.close()

    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404

    # Convert the query result to a dictionary
    return jsonify(dict(employee))

# Custom 404 error handler


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404

# Custom 500 error handler


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'Internal error, check logs'}), 500


# mainline
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3639, debug=True)
