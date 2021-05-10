import os

import mysql as mysql
import mysql.connector
import pandas as pd
import json

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\files\\studentProgress.csv"
print(filepath)
data = pd.read_csv(filepath, delimiter=';', encoding='utf-8')

df = pd.DataFrame(data,
                  columns=['Студент', 'Группа', 'Дисциплина', 'Семестр', 'УчебныйГод', 'Оценка', 'Специальность',
                           'ФормаОбучения', 'Квалификация', 'Статус'])

print(df)

subjects = []

for i, ii in enumerate(df['Дисциплина']):
    if not (df['Дисциплина'][i] in subjects):
        subjects.append(df['Дисциплина'][i])

print(subjects)

# with open('../files/subjects.txt', 'w') as f:
#     for item in subjects:
#         f.write("%s\n" % item)

conn = mysql.connector.connect(host='46.229.214.191',
                               database='trajectories_test',
                               user='testuser',
                               password='testuser')
if conn.is_connected():
    print('Connected to MySQL database')

# conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
#                       'Server=LAPTOP-87B1DRMT;'
#                       'Database=vkr;'
#                       'Trusted_Connection=yes;')
# cursor = conn.cursor()
#
# conn.execute('CREATE TABLE Оценки(ID nvarchar(60) NOT NULL, Группа nvarchar(60), Дисциплина nvarchar(300),'
#              'Семестр nvarchar(2),'
#              'УчебныйГод nvarchar(9),'
#              'Оценка nvarchar(20),'
#              'Специальность nvarchar(300),'
#              'ФормаОбучения nvarchar(50),'
#              'Квалификация nvarchar(50),'
#              'Статус nvarchar(50))')

# for i, ii in enumerate(df['Оценка']):
#     if df['Оценка'][i] == 'отлично':
#         df['Оценка'][i] = 5
#     if df['Оценка'][i] == 'хорошо':
#         df['Оценка'][i] = 4
#     if df['Оценка'][i] == 'удовлетворительно':
#         df['Оценка'][i] = 3
#     if df['Оценка'][i] == 'неудовлетворительно':
#         df['Оценка'][i] = 2


# for row in df.itertuples():
#     cursor.execute('''
#                           INSERT INTO vkr.dbo.Оценки (ID, Группа, Дисциплина, Семестр, УчебныйГод, Оценка, Специальность,
#                            ФормаОбучения, Квалификация, Статус)
#                          VALUES (?,?,?,?,?,?,?,?,?,?)
#                            ''',
#                    row.Студент,
#                    row.Группа,
#                    row.Дисциплина,
#                    row.Семестр,
#                    row.УчебныйГод,
#                    row.Оценка,
#                    row.Специальность,
#                    row.ФормаОбучения,
#                    row.Квалификация,
#                    row.Статус
#                    )
