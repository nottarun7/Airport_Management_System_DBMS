import psycopg2
import os
from tabulate import tabulate  # You'll need to pip install tabulate

def connect_to_db():
    """Establish connection to the database"""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "airport_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "swaha"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432")
        )
        print("✓ Connected to database successfully")
        return conn
    except Exception as e:
        print(f"✗ Database connection error: {e}")
        return None

def execute_query(query, params=None, fetch=True):
    """Execute an SQL query and return results if applicable"""
    conn = connect_to_db()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        
        if fetch:
            # Get column names from cursor description
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            
            # Display results in a formatted table
            print(tabulate(rows, headers=columns, tablefmt="psql"))
            return rows, columns
        else:
            # For INSERT, UPDATE, DELETE operations
            affected_rows = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            print(f"✓ Query executed successfully. Rows affected: {affected_rows}")
            return affected_rows
            
    except Exception as e:
        conn.rollback()
        cursor.close()
        conn.close()
        print(f"✗ Query execution error: {e}")
        return None

def examples():
    """Example CRUD operations using SQL"""
    print("\n==== CREATE (INSERT) Example ====")
    insert_query = """
    INSERT INTO Passengers (Name, Passport_Number, Nationality, Gender, DOB) 
    VALUES (%s, %s, %s, %s, %s) 
    RETURNING *
    """
    params = ("John Smith", "US123456", "American", "Male", "1990-05-15")
    result = execute_query(insert_query, params, fetch=True)
    
    # Store the ID of the newly created passenger for later examples
    passenger_id = None
    if result and result[0] and len(result[0]) > 0:
        passenger_id = result[0][0][0]  # First row, first column (Passenger_ID)
    
    print("\n==== READ (SELECT) Example ====")
    select_query = """
    SELECT Passenger_ID, Name, Passport_Number, Nationality 
    FROM Passengers 
    ORDER BY Passenger_ID DESC
    LIMIT 5
    """
    execute_query(select_query)
    
    if passenger_id:
        print("\n==== UPDATE Example ====")
        update_query = """
        UPDATE Passengers 
        SET Nationality = %s 
        WHERE Passenger_ID = %s 
        RETURNING *
        """
        execute_query(update_query, ("Canadian", passenger_id), fetch=True)
    
        print("\n==== DELETE Example ====")
        delete_query = "DELETE FROM Passengers WHERE Passenger_ID = %s"
        execute_query(delete_query, (passenger_id,), fetch=False)

def custom_query():
    """Run a custom SQL query from user input"""
    print("\n==== Custom SQL Query Tool ====")
    print("Enter your SQL query (type 'exit' to quit):")
    
    while True:
        # Get multiline input until a semicolon is found
        lines = []
        while True:
            line = input("> " if not lines else "... ")
            if line.lower() == 'exit':
                return
            lines.append(line)
            if line.strip().endswith(';'):
                break
        
        query = ' '.join(lines).strip()
        if not query:
            continue
            
        # Remove trailing semicolon for psycopg2
        if query.endswith(';'):
            query = query[:-1]
            
        # Determine if this is a SELECT query or a modification query
        is_select = query.lower().lstrip().startswith(('select', 'with', 'show'))
        execute_query(query, fetch=is_select)

if __name__ == "__main__":
    print("===== SQL Query Tool for Airport Management System =====")
    print("1. Run CRUD examples")
    print("2. Execute custom SQL queries")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ")
    
    if choice == '1':
        examples()
    elif choice == '2':
        custom_query()
    else:
        print("Exiting...")