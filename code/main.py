import os
import mysql.connector
import pandas as pd

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\files\\studentProgress.csv"
print(filepath)
data = pd.read_csv(filepath, delimiter=';', encoding='utf-8')

df = pd.DataFrame(data,
                  columns=['Студент', 'Группа', 'Дисциплина', 'Семестр', 'УчебныйГод', 'Оценка', 'Специальность',
                           'ФормаОбучения', 'Квалификация', 'Статус'])

df = df.fillna(0)
#print(df)
df1 = pd.DataFrame()

# subjects = []
# for i, ii in enumerate(df['Дисциплина']):
#     if not (df['Дисциплина'][i] in subjects):
#         subjects.append(df['Дисциплина'][i])
# print(subjects)

# with open('../files/subjects.txt', 'w') as f:
#     for item in subjects:
#         f.write("%s\n" % item)

conn = mysql.connector.connect(host='46.229.214.191',
                               database='trajectories_test',
                               user='testuser',
                               password='testuser')
if conn.is_connected():
    print('Connected to MySQL database')

# for i, ii in enumerate(df['Оценка']):
#     if df['Оценка'][i] == 'отлично':
#         df['Оценка'][i] = 5
#     if df['Оценка'][i] == 'хорошо':
#         df['Оценка'][i] = 4
#     if df['Оценка'][i] == 'удовлетворительно':
#         df['Оценка'][i] = 3
#     if df['Оценка'][i] == 'неудовлетворительно':
#         df['Оценка'][i] = 2

existGroups = []
existStudents = []
existDisciplines = []

i = 1

cursor = conn.cursor()

# for row in df.itertuples():
#     if not row.Группа in existGroups:
#         cursor.execute(
#             "INSERT INTO `groups` (groups_id, major, form_of_education, qualificaion) VALUES ( %s, %s, %s, %s )",
#             [row.Группа,
#              row.Специальность,
#              row.ФормаОбучения,
#              row.Квалификация])
#         existGroups.append(row.Группа)
#
# for row in df.itertuples():
#     if not row.Студент in existStudents:
#         cursor.execute("INSERT INTO `students` (students_id, status, groups_id) VALUES ( %s, %s, %s)",
#                    [row.Студент,
#                     row.Статус,
#                     row.Группа])
#         existStudents.append(row.Студент)

# for row in df.itertuples():
#     if not row.Дисциплина in existDisciplines:
#         cursor.execute("INSERT INTO disciplines (disciplines_id, name) VALUES ( %s, %s)",
#                    [i,
#                     row.Дисциплина])
#         existDisciplines.append(row.Дисциплина)
#     i += 1

# for row in df.itertuples():
#     cursor.execute("INSERT INTO marks (mark, `year`, semestr, students_id, disciplines_id) VALUES ( %s, %s, %s, %s, %s )",
#                    [row.Оценка,
#                     row.УчебныйГод,
#                     row.Семестр,
#                     row.Студент,
#                     row.Дисциплина])  # здесь нужен id, у нас название


for row in df.itertuples():
        cursor.execute(
            "INSERT INTO marks (mark, year, semestr, students_id, disciplines_id) VALUES (%s, %s, %s, %s, (SELECT disciplines_id FROM disciplines WHERE name = %s))",
            [row.Оценка,
             row.УчебныйГод,
             row.Семестр,
             row.Студент,
             row.Дисциплина])  # здесь нужен id, у нас название

conn.commit()

