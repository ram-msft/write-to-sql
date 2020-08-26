# Example script using read/write to azure sql database table
# this script is using cursors, but we can use SQLAlchemy and avoid dealing with cursors
import pyodbc

# retain the curly braces in your connection script.
# you can also copy the connection string directly from Azure Portal
with pyodbc.connect(
    r'Driver={ODBC Driver 17 for SQL Server};'
    r'Server=tcp:<server_name>.database.windows.net,1433;'
    r'Database=<database_name>;'
    r'Uid=<user_id>;'
    r'Pwd={<user_password>};'
    r'Encrypt=yes;'
    r'TrustServerCertificate=no;'
    r'Connection Timeout=30;'
) as cnxn:
    cursor = cnxn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pyodbc_demo")
    initial = cursor.fetchone()[0]
    cursor.execute("INSERT INTO pyodbc_demo VALUES ('Sample Name 5', '45')")
    cursor.execute("SELECT COUNT(*) FROM pyodbc_demo")
    final = cursor.fetchone()[0]
    print("Initial row count: {}\nFinal row count: {}\nInsert Successful: {}".format(initial, final, (final-initial == 1)))