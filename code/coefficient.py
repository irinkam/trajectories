import os
import pandas as pd
import mysql.connector

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\files\\disciplines_10.csv"
data = pd.read_csv(filepath, delimiter=';', encoding='utf-8')

df_1 = pd.DataFrame(data, columns=['number', 'disciplines_id', 'avgMark'])
df_2 = df_1

list_of_disciplines = []

coefficient = 0
i = 0

for row_1 in df_1.itertuples():
    for row_2 in df_2.itertuples():
        if row_1.disciplines_id == row_2.disciplines_id: continue
        coefficient = row_1.avgMark / row_2.avgMark
        if coefficient > 1: coefficient = 1 / coefficient
        list_of_disciplines.append([row_1.disciplines_id, row_2.disciplines_id, coefficient])
    df_2 = df_2.drop(i)
    i += 1

conn = mysql.connector.connect(host='46.229.214.191',
                               database='trajectories_test',
                               user='testuser',
                               password='testuser')

cursor = conn.cursor()

x = 0

for x in range(0, 1010000, 10000):
    cursor.executemany("""
            insert into new_connection_of_disciplines
            (first_discipline_id, second_discipline_id, weight)
            values (%s, %s, %s)""", list_of_disciplines[0 + x : x + 10000])

conn.commit()