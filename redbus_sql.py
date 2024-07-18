import sqlite3

def create_database():
    conn = sqlite3.connect('redbus.db')
    c = conn.cursor()

    # Create table
    c.execute('''
    CREATE TABLE IF NOT EXISTS redbuscsv (
        route_name TEXT,
        route_url TEXT,
        bus_name TEXT,
        departure TEXT,
        arrival TEXT,
        depart_time TEXT,
        arrival_time TEXT,
        duration TEXT,
        bus_type TEXT,
        star_rating TEXT,
        price TEXT,
        seats_available TEXT
    )
    ''')

    # Commit and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database and table
create_database()
