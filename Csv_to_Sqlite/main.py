import sqlite3
import pandas as pd

#taking data from csv
data = pd.read_csv('diabetes.csv')

data_list = []
for i in range(len(data)):
    row_list = (data.loc[i, :].values.flatten().tolist())
    data_list.append(row_list)

#creating database
conn = sqlite3.connect('test.db')
print('Database created.')

cursor = conn.cursor()
print('Cursor created.')

cursor.execute("""DROP TABLE DIABETES""")

#creating data table
cursor.execute(""" CREATE TABLE IF NOT EXISTS DIABETES(
    Pregnancies DOUBLE,
    Glucose DOUBLE,
    BloodPressure DOUBLE,
    SkinThickness DOUBLE,
    Insulin DOUBLE,
    BMI DOUBLE,
    DiabetesPedigreeFunction DOUBLE,
    Age DOUBLE,
    Outcome DOUBLE
) """)

#Adding data to database
add_data = """INSERT INTO DIABETES VALUES (?,?,?,?,?,?,?,?,?)"""
cursor.executemany(add_data,data_list)
print('Data added to DataBase')

conn.commit()
conn.close()
print('Database is closed')