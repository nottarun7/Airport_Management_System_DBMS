# Airport Management System

## Overview
This project demonstrates an airport database management system using a PostgreSQL backend, a Flask API for CRUD operations, and a web-based frontend for data entry and viewing. Additionally, it includes a SQL query tool (`shell.py`) that allows manual SQL query execution for further interaction with the database.

## DBMS Concepts Demonstrated

### 1. Relational Database Design
- **Tables & Relationships**: The system organizes data into normalized tables—**Passengers**, **Flights**, and **Tickets**—to minimize redundancy and ensure data integrity.
- **Primary Keys**: Each table uses a primary key (e.g., `Passenger_ID`, `Flight_ID`, `Ticket_ID`) to uniquely identify records.

### 2. CRUD Operations
- **Create**: Use SQL `INSERT` statements to add new records.  
- **Read**: Use SQL `SELECT` statements to retrieve data for display.  
- **Update**: Use SQL `UPDATE` statements to modify existing records.  
- **Delete**: Use SQL `DELETE` statements to remove records from the database.

### 3. Transactions and ACID Properties
- **Transactions**: The project commits operations to ensure consistency. In the event of errors, operations are rolled back to maintain integrity.

### 4. Direct SQL Query Execution
- **SQL Query Tool (`shell.py`)**: This file demonstrates how to execute custom SQL queries using `psycopg2` and displays results in formatted tables using the `tabulate` library. It includes examples for each CRUD operation.

## Project Structure

```
Airport_management_system
├── backend
│   ├── app.py         # Flask API endpoints for CRUD operations
│   ├── db_config.py   # Database connection configuration using psycopg2
│   └── requirements.txt
├── frontend
│   ├── index.html     # Main HTML for the user interface
│   ├── scripts.js     # JavaScript for dynamic UI and form handling
│   └── styles.css     # CSS for styling the frontend
├── shell.py           # SQL query tool for running manual queries
└── init_db.sql        # SQL script for initializing the database schema
```

## How to Run the Project

### Prerequisites
- **Python 3.x**  
- **PostgreSQL** database  
- **pip** for installing Python packages

### 1. Running the Backend
1. **Navigate to the Backend Directory:**
   ```shell
   cd c:\Projects\Airport_management_system\backend
   ```

2. **Install Dependencies:**
   ```shell
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Ensure there is a `.env` file at the project root (or configure environment variables in your system) with:
   ```
   DB_NAME=airport_db
   DB_USER=postgres
   DB_PASS=swaha
   DB_HOST=localhost
   DB_PORT=5432
   ```
   
4. **Initialize the Database:**
   Run the `init_db.sql` script in your PostgreSQL database to create the necessary tables.

5. **Start the Flask Server:**
   ```shell
   python app.py
   ```
   The Flask application will run (by default on http://127.0.0.1:5000).

### 2. Running the Frontend
1. **Navigate to the Frontend Directory:**
   ```shell
   cd c:\Projects\Airport_management_system\frontend
   ```

2. **Open `index.html`:**
   Open `index.html` directly in your browser, or use a live server (e.g., VS Code Live Server extension) to serve the file.

### 3. Running the SQL Query Tool (`shell.py`)
1. **Run Shell Script:**
   In a terminal at the project's root, execute:
   ```shell
   python shell.py
   ```

2. **Using the Tool:**
   - **Option 1:** Run sample CRUD examples.
   - **Option 2:** Execute custom SQL queries interactively.
   - **Option 3:** Exit the tool.

## Conclusion
This project integrates key DBMS concepts such as relational schema design, CRUD operations, transactional processing, and direct SQL execution. It offers both a user-friendly web frontend and a command-line SQL tool, making it an excellent learning platform and a solid foundation for further enhancements.
