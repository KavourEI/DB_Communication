import sqlite3
import json

df_file = 'local_database.db'    # The DB file created from earlier, containing all the precious data of yours! 

conn = sqlite3.connect(df_file)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")    # Get all the table names in the database
tables = cursor.fetchall()
tables

tables_info = {}    # Hmmm mind that here! We are going to fill this object with the included features.

for feature in tables:    # Iterate to collect feature names, yes at this point just feature names! 
    table_name = feature[0]
    cursor.execute("PRAGMA table_info('{}')".format(table_name))
    columns = cursor.fetchall()
    columns_info = []
    for column in columns:
        column_name = column[1]
        column_type = column[2]
        columns_info.append({'name': column_name, 'type': column_type})
    tables_info[table_name] = columns_info

conn.close()

with open(f'{df_file.split('.')[0]}.json', 'w') as json_file:
    json.dump(tables_info, json_file, indent=4)    # Export information to a json file.

print(f"Table information has been exported to {df_file.split('.')[0]}.json")
