import sqlite3
import json

df_file = 'local_database.db'

# Connect to the SQLite database
conn = sqlite3.connect(df_file)
cursor = conn.cursor()

# Get the table names in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
tables
# Dictionary to store table information
tables_info = {}

# Iterate over tables
for feature in tables:
    table_name = feature[0]
    cursor.execute("PRAGMA table_info('{}')".format(table_name))
    columns = cursor.fetchall()
    columns_info = []
    for column in columns:
        column_name = column[1]
        column_type = column[2]
        columns_info.append({'name': column_name, 'type': column_type})
    tables_info[table_name] = columns_info

# Close the connection
conn.close()

# Write table information to a JSON file
with open(f'{df_file.split('.')[0]}.json', 'w') as json_file:
    json.dump(tables_info, json_file, indent=4)

print("Table information has been exported to database_info.json")
