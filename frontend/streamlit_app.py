# streamlit_app.py
import streamlit as st
import psycopg2
import pandas as pd
from psycopg2.extras import RealDictCursor
from datetime import datetime, time, timedelta

# --- Set page config first, before any other Streamlit commands ---
st.set_page_config(page_title="Airport Management System", layout="wide")

# --- Database Connection ---
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        database="Airport_DBMS",
        user="postgres",
        password="swaha",
        host="localhost",
        port="5432"
    )

conn = get_connection()

# --- Helper Functions ---
def fetch_table(table):
    return pd.read_sql(f"SELECT * FROM {table}", conn)

def execute_query(query, params):
    with conn.cursor() as cur:
        cur.execute(query, params)
        conn.commit()

# --- Streamlit App ---
st.title("✈️ Airport Management System")

tabs = st.tabs(["Passengers", "Flights", "Tickets", "Baggage"])

# --- Passengers Tab ---
with tabs[0]:
    st.subheader("Manage Passengers")
    df_passengers = fetch_table('Passengers')
    st.dataframe(df_passengers, use_container_width=True)
    with st.expander("Add / Update / Delete Passenger"):
        mode = st.selectbox("Action", ["Create", "Update", "Delete"], key="passenger_mode")
        name = st.text_input("Name", key="passenger_name")
        passport = st.text_input("Passport Number", key="passenger_passport")
        nationality = st.text_input("Nationality", key="passenger_nationality")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="passenger_gender")
        dob = st.date_input("Date of Birth", key="passenger_dob")
        if mode != "Create":
            pid = st.number_input("Passenger ID", min_value=1, step=1, key="passenger_id")
        if st.button(f"{mode} Passenger", key="passenger_button"):
            if mode == "Create":
                execute_query(
                    "INSERT INTO Passengers (Name, Passport_Number, Nationality, Gender, DOB) VALUES (%s,%s,%s,%s,%s)",
                    (name, passport, nationality, gender, dob)
                )
                st.success("Passenger created")
            elif mode == "Update":
                execute_query(
                    "UPDATE Passengers SET Name=%s, Passport_Number=%s, Nationality=%s, Gender=%s, DOB=%s WHERE Passenger_ID=%s",
                    (name, passport, nationality, gender, dob, pid)
                )
                st.success("Passenger updated")
            else:
                execute_query(
                    "DELETE FROM Passengers WHERE Passenger_ID=%s",
                    (pid,)
                )
                st.success("Passenger deleted")

# --- Flights Tab ---
with tabs[1]:
    st.subheader("Manage Flights")
    df_flights = fetch_table('Flights')
    st.dataframe(df_flights, use_container_width=True)
    with st.expander("Add / Update / Delete Flight"):
        mode = st.selectbox("Action", ["Create", "Update", "Delete"], key="flight_mode")
        number = st.text_input("Flight Number", key="flight_number")
        source = st.text_input("Source", key="flight_source")
        dest = st.text_input("Destination", key="flight_dest")
        
        # Replace datetime_input with separate date and time inputs
        dep_date = st.date_input("Departure Date", key="flight_dep_date")
        dep_time = st.time_input("Departure Time", key="flight_dep_time")
        # Combine date and time
        dep = datetime.combine(dep_date, dep_time)
        
        arr_date = st.date_input("Arrival Date", key="flight_arr_date")
        arr_time = st.time_input("Arrival Time", key="flight_arr_time")
        # Combine date and time
        arr = datetime.combine(arr_date, arr_time)
        
        if mode != "Create":
            fid = st.number_input("Flight ID", min_value=1, step=1, key="flight_id")
        if st.button(f"{mode} Flight", key="flight_button"):
            if mode == "Create":
                execute_query(
                    "INSERT INTO Flights (Flight_Number, Source, Destination, Departure_Time, Arrival_Time) VALUES (%s,%s,%s,%s,%s)",
                    (number, source, dest, dep, arr)
                )
                st.success("Flight created")
            elif mode == "Update":
                execute_query(
                    "UPDATE Flights SET Flight_Number=%s, Source=%s, Destination=%s, Departure_Time=%s, Arrival_Time=%s WHERE Flight_ID=%s",
                    (number, source, dest, dep, arr, fid)
                )
                st.success("Flight updated")
            else:
                execute_query(
                    "DELETE FROM Flights WHERE Flight_ID=%s",
                    (fid,)
                )
                st.success("Flight deleted")

# --- Tickets Tab ---
with tabs[2]:
    st.subheader("Manage Tickets")
    df_tickets = fetch_table('Tickets')
    st.dataframe(df_tickets, use_container_width=True)
    with st.expander("Add / Update / Delete Ticket"):
        mode = st.selectbox("Action", ["Create", "Update", "Delete"], key="ticket_mode")
        pid = st.number_input("Passenger ID", min_value=1, step=1, key="ticket_pid")
        fid = st.number_input("Flight ID", min_value=1, step=1, key="ticket_fid")
        seat = st.text_input("Seat Number", key="ticket_seat")
        tclass = st.text_input("Travel Class", key="ticket_class")
        price = st.number_input("Price", min_value=0.0, step=0.01, key="ticket_price")
        if mode != "Create":
            tid = st.number_input("Ticket ID", min_value=1, step=1, key="ticket_id")
        if st.button(f"{mode} Ticket", key="ticket_button"):
            if mode == "Create":
                execute_query(
                    "INSERT INTO Tickets (Passenger_ID, Flight_ID, Seat_Number, Travel_Class, Price) VALUES (%s,%s,%s,%s,%s)",
                    (pid, fid, seat, tclass, price)
                )
                st.success("Ticket created")
            elif mode == "Update":
                execute_query(
                    "UPDATE Tickets SET Passenger_ID=%s, Flight_ID=%s, Seat_Number=%s, Travel_Class=%s, Price=%s WHERE Ticket_ID=%s",
                    (pid, fid, seat, tclass, price, tid)
                )
                st.success("Ticket updated")
            else:
                execute_query(
                    "DELETE FROM Tickets WHERE Ticket_ID=%s",
                    (tid,)
                )
                st.success("Ticket deleted")

# --- Baggage Tab ---
with tabs[3]:
    st.subheader("Manage Baggage")
    df_baggage = fetch_table('Baggage')
    st.dataframe(df_baggage, use_container_width=True)
    with st.expander("Add / Update / Delete Baggage"):
        mode = st.selectbox("Action", ["Create", "Update", "Delete"], key="baggage_mode")
        pid_bg = st.number_input("Passenger ID", min_value=1, step=1, key="baggage_pid")
        weight = st.number_input("Weight", min_value=0.0, step=0.1, key="baggage_weight")
        tag = st.text_input("Tag ID", key="baggage_tag")
        if mode != "Create":
            bid = st.number_input("Baggage ID", min_value=1, step=1, key="baggage_id")
        if st.button(f"{mode} Baggage", key="baggage_button"):
            if mode == "Create":
                execute_query(
                    "INSERT INTO Baggage (Passenger_ID, Weight, Tag_ID) VALUES (%s,%s,%s)",
                    (pid_bg, weight, tag)
                )
                st.success("Baggage created")
            elif mode == "Update":
                execute_query(
                    "UPDATE Baggage SET Passenger_ID=%s, Weight=%s, Tag_ID=%s WHERE Baggage_ID=%s",
                    (pid_bg, weight, tag, bid)
                )
                st.success("Baggage updated")
            else:
                execute_query(
                    "DELETE FROM Baggage WHERE Baggage_ID=%s",
                    (bid,)
                )
                st.success("Baggage deleted")
