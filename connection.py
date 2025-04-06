import pyodbc

def get_connection():
    conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=users;'
    'Trusted_Connection=yes;'
    )
    return conn

def insert_data(conn, firstname, lastname, mobile):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO NewTable (firstname, lastname, mobile) VALUES (?, ?, ?)",
                   (firstname, lastname, mobile))
    conn.commit()
    cursor.close()
    print("Data inserted successfully.")
    
def fetch_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM NewTable")
    columns = [column[0] for column in cursor.description]  # Get column names
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]      # Convert each row to a dict
    cursor.close()
    return result

# Example usage
# conn = get_connection()
# insert_data(conn, 'John', 'Doe', '1234567890')
# print(fetch_data(conn))
