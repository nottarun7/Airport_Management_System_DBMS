from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME", "airport_db"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASS", "swaha"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432")
)
cursor = conn.cursor()

@app.route('/passengers', methods=['GET'])
def get_passengers():
    cursor.execute("SELECT * FROM Passengers")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return jsonify([dict(zip(columns, row)) for row in rows])

@app.route('/passengers', methods=['POST'])
def add_passenger():
    data = request.json
    cursor.execute("""
        INSERT INTO Passengers (Name, Passport_Number, Nationality, Gender, DOB)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING *
    """, (data['name'], data['passport'], data['nationality'], data['gender'], data['dob']))
    conn.commit()
    return jsonify(cursor.fetchone())

@app.route('/passengers/<int:id>', methods=['DELETE'])
def delete_passenger(id):
    cursor.execute("DELETE FROM Passengers WHERE Passenger_ID = %s", (id,))
    conn.commit()
    return '', 204

@app.route('/flights', methods=['GET'])
def get_flights():
    cursor.execute("SELECT * FROM Flights")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return jsonify([dict(zip(columns, row)) for row in rows])

@app.route('/flights', methods=['POST'])
def add_flight():
    data = request.json
    cursor.execute("""
        INSERT INTO Flights (Airline_ID, Source, Destination, Departure_Time, Arrival_Time, Status)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING *
    """, (data['airline_id'], data['source'], data['destination'], data['departure_time'], data['arrival_time'], data['status']))
    conn.commit()
    return jsonify(cursor.fetchone())

@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    cursor.execute("DELETE FROM Flights WHERE Flight_ID = %s", (id,))
    conn.commit()
    return '', 204

@app.route('/tickets', methods=['GET'])
def get_tickets():
    cursor.execute("SELECT * FROM Tickets")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return jsonify([dict(zip(columns, row)) for row in rows])

@app.route('/tickets', methods=['POST'])
def book_ticket():
    data = request.json
    cursor.execute("""
        INSERT INTO Tickets (Passenger_ID, Flight_ID, Seat_Number, Class, Price, Booking_Date)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING *
    """, (data['passenger_id'], data['flight_id'], data['seat_number'], data['class'], data['price'], data['booking_date']))
    conn.commit()
    return jsonify(cursor.fetchone())

@app.route('/tickets/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    cursor.execute("DELETE FROM Tickets WHERE Ticket_ID = %s", (id,))
    conn.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)