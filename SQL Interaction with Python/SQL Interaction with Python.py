#  Kyle Harris
#  CIT-117/117L Python
#  SQL Database Interaction with Python

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Retirement.db')
cursor = conn.cursor()

# Create tables with IF NOT EXISTS
cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Pay (
    EmployeeID INTEGER,
    Year INTEGER,
    Earnings REAL,
    FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS SocialSecurityMin (
    Year INTEGER PRIMARY KEY,
    Minimum REAL
)''')

print("Tables created successfully.")

# Step 2:

# Import Employee.txt data
with open('Employee.txt', 'r') as file:
    next(file)  # Skip the header row
    for line in file:
        values = tuple(line.strip().split(','))
        # Check if EmployeeID already exists
        cursor.execute("SELECT COUNT(*) FROM Employee WHERE EmployeeID = ?", (values[0],))
        if cursor.fetchone()[0] == 0:  # Only insert if EmployeeID doesn't exist
            query = "INSERT INTO Employee (EmployeeID, Name) VALUES (?, ?)"
            cursor.execute(query, values)

# Import Pay.txt data
with open('Pay.txt', 'r') as file:
    next(file)  # Skip the header row
    for line in file:
        values = tuple(line.strip().split(','))
        # Check if record already exists
        cursor.execute("SELECT COUNT(*) FROM Pay WHERE EmployeeID = ? AND Year = ?", (values[0], values[1]))
        if cursor.fetchone()[0] == 0:  # Only insert if the record doesn't exist
            query = "INSERT INTO Pay (EmployeeID, Year, Earnings) VALUES (?, ?, ?)"
            cursor.execute(query, values)

# Import SocialSecurityMinimum.txt data
with open('SocialSecurityMinimum.txt', 'r') as file:
    next(file)  # Skip the header row
    for line in file:
        values = tuple(line.strip().split(','))
        # Check if Year already exists
        cursor.execute("SELECT COUNT(*) FROM SocialSecurityMin WHERE Year = ?", (values[0],))
        if cursor.fetchone()[0] == 0:  # Only insert if Year doesn't exist
            query = "INSERT INTO SocialSecurityMin (Year, Minimum) VALUES (?, ?)"
            cursor.execute(query, values)


# Commit changes
conn.commit()
print("Data imported successfully.")

# Step 3: Data Reporting Logic
query = '''
SELECT e.Name, p.Year, p.Earnings, s.Minimum
FROM Employee e
JOIN Pay p ON e.EmployeeID = p.EmployeeID
JOIN SocialSecurityMin s ON p.Year = s.Year
'''

cursor.execute(query)
results = cursor.fetchall()

# Process records and determine retirement eligibility
print("") # Print new line (I know, I know... Use \n for new line but this was easier for formatting at the moment.)
print(f"{'Name':<15} {'Year':<6} {'Earnings':<10} {'Minimum':<10} {'Eligible':<8}")
print("-" * 50) # This is a neat way to make a line --------------------------------
for row in results:
    name, year, earnings, minimum = row
    result = "Yes" if earnings >= minimum else "No"
    print(f"{name:<15} {year:<6} {earnings:<10.2f} {minimum:<10.2f} {result:<8}")

# Prevents Program from duplicating the database everytime the program runs (This was a problem for some reason)
cursor.execute("DELETE FROM Employee")
cursor.execute("DELETE FROM Pay")
cursor.execute("DELETE FROM SocialSecurityMin")
conn.commit()

print("\nTables cleared.")

# Close connection
conn.close()

#  Prevents the program from closing.
input("\nPress Enter to exit...")