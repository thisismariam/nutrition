import pandas as pd
import sqlite3

def csv_to_sql(csv_file_path, db_name, table_name):
    # Step 1: Read data from CSV file using pandas
    df = pd.read_csv(csv_file_path)

    # Step 2: Create an SQLite database and connect to it
    conn = sqlite3.connect(db_name)

    # Step 3: Write the DataFrame to an SQL table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

# Example usage:
csv_file_path = 'nutrition.csv'
db_name = 'Nutrition.db'
table_name = 'Nutritiontable'
csv_to_sql(csv_file_path, db_name, table_name)
