# app.py
from flask import Flask, request, jsonify, render_template
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# PostgreSQL Connection
conn = psycopg2.connect(
    database="Airport_DBMS",
    user="postgres",
    password="swaha",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

# === PASSENGERS ===
@app.route('/passengers', methods=['GET'])
def get_passengers():
    cur.execute("SELECT * FROM Passengers")
    return jsonify(cur.fetchall())

@app.route('/passenger', methods=['POST'])
def add_passenger():
    data = request.json
    cur.execute("""
        INSERT INTO Passengers (Name, Passport_Number, Nationality, Gender, DOB)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['name'], data['passport'], data['nationality'], data['gender'], data['dob']))
    conn.commit()
    return jsonify({'message': 'Passenger added'})

@app.route('/passenger/<int:id>', methods=['PUT'])
def update_passenger(id):
    data = request.json
    cur.execute("""
        UPDATE Passengers SET Name=%s, Passport_Number=%s, Nationality=%s, Gender=%s, DOB=%s
        WHERE Passenger_ID=%s
    """, (data['name'], data['passport'], data['nationality'], data['gender'], data['dob'], id))
    conn.commit()
    return jsonify({'message': 'Passenger updated'})

@app.route('/passenger/<int:id>', methods=['DELETE'])
def delete_passenger(id):
    cur.execute("DELETE FROM Passengers WHERE Passenger_ID=%s", (id,))
    conn.commit()
    return jsonify({'message': 'Passenger deleted'})

# === FLIGHTS ===
@app.route('/flights', methods=['GET'])
def get_flights():
    cur.execute("SELECT * FROM Flights")
    return jsonify(cur.fetchall())

@app.route('/flight', methods=['POST'])
def add_flight():
    data = request.json
    cur.execute("""
        INSERT INTO Flights (Flight_Number, Source, Destination, Departure_Time, Arrival_Time)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['number'], data['source'], data['dest'], data['dep'], data['arr']))
    conn.commit()
    return jsonify({'message': 'Flight added'})

@app.route('/flight/<int:id>', methods=['PUT'])
def update_flight(id):
    data = request.json
    cur.execute("""
        UPDATE Flights SET Flight_Number=%s, Source=%s, Destination=%s,
        Departure_Time=%s, Arrival_Time=%s WHERE Flight_ID=%s
    """, (data['number'], data['source'], data['dest'], data['dep'], data['arr'], id))
    conn.commit()
    return jsonify({'message': 'Flight updated'})

@app.route('/flight/<int:id>', methods=['DELETE'])
def delete_flight(id):
    cur.execute("DELETE FROM Flights WHERE Flight_ID=%s", (id,))
    conn.commit()
    return jsonify({'message': 'Flight deleted'})

# === TICKETS ===
@app.route('/tickets', methods=['GET'])
def get_tickets():
    cur.execute("SELECT * FROM Tickets")
    return jsonify(cur.fetchall())

@app.route('/ticket', methods=['POST'])
def add_ticket():
    data = request.json
    cur.execute("""
        INSERT INTO Tickets (Passenger_ID, Flight_ID, Seat_Number, Travel_Class, Price)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['pid'], data['fid'], data['seat'], data['class'], data['price']))
    conn.commit()
    return jsonify({'message': 'Ticket added'})

@app.route('/ticket/<int:id>', methods=['PUT'])
def update_ticket(id):
    data = request.json
    cur.execute("""
        UPDATE Tickets SET Passenger_ID=%s, Flight_ID=%s, Seat_Number=%s,
        Travel_Class=%s, Price=%s WHERE Ticket_ID=%s
    """, (data['pid'], data['fid'], data['seat'], data['class'], data['price'], id))
    conn.commit()
    return jsonify({'message': 'Ticket updated'})

@app.route('/ticket/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    cur.execute("DELETE FROM Tickets WHERE Ticket_ID=%s", (id,))
    conn.commit()
    return jsonify({'message': 'Ticket deleted'})

# === BAGGAGE ===
@app.route('/baggage', methods=['GET'])
def get_baggage():
    cur.execute("SELECT * FROM Baggage")
    return jsonify(cur.fetchall())

@app.route('/baggage', methods=['POST'])
def add_baggage():
    data = request.json
    cur.execute("""
        INSERT INTO Baggage (Passenger_ID, Weight, Tag_ID)
        VALUES (%s, %s, %s)
    """, (data['pid'], data['weight'], data['tag']))
    conn.commit()
    return jsonify({'message': 'Baggage added'})

@app.route('/baggage/<int:id>', methods=['PUT'])
def update_baggage(id):
    data = request.json
    cur.execute("""
        UPDATE Baggage SET Passenger_ID=%s, Weight=%s, Tag_ID=%s WHERE Baggage_ID=%s
    """, (data['pid'], data['weight'], data['tag'], id))
    conn.commit()
    return jsonify({'message': 'Baggage updated'})

@app.route('/baggage/<int:id>', methods=['DELETE'])
def delete_baggage(id):
    cur.execute("DELETE FROM Baggage WHERE Baggage_ID=%s", (id,))
    conn.commit()
    return jsonify({'message': 'Baggage deleted'})

if __name__ == '__main__':
    app.run(debug=True)
