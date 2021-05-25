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

# existGroups = []
# existStudents = []
# existDisciplines = []

i = 1

cursor = conn.cursor()

# for row in df.itertuples():
#     if not row.Группа in existGroups:
#         cursor.execute(
#             "INSERT INTO groups (groups_id, major, form_of_education, qualificaion) VALUES ( %s, %s, %s, %s )",
#             [row.Группа,
#              row.Специальность,
#              row.ФормаОбучения,
#              row.Квалификация])
#         existGroups.append(row.Группа)
#
# for row in df.itertuples():
#     if not row.Студент in existStudents:
#         cursor.execute("INSERT INTO students (students_id, status, groups_id) VALUES ( %s, %s, %s)",
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

for row in df.itertuples():
    if not row.Оценка == 'зачтено' or not row.Оценка == 'незачет':
        cursor.execute(
            "INSERT INTO new_marks (mark, year, semestr, students_id, disciplines_id) VALUES (%s, %s, %s, %s, (SELECT disciplines_id FROM new_disciplines WHERE name = %s))",
            [row.Оценка,
             row.УчебныйГод,
             row.Семестр,
             row.Студент,
             row.Дисциплина])
        conn.commit()

for row in df.itertuples():
    cursor.execute(
        "INSERT INTO new_connection_of_disciplines (connection_id, first_discipline_id, second_discipline_id, weight)"
        "VALUES (%s, %s, %s, %s, (select smth.disciplines_id, new_disciplines.disciplines_id, smth.avgMark / new_disciplines.avgMark "
        "from new_disciplines cross join (select disciplines_id, avgMark from new_disciplines) as smth))"
        "where disciplines.name <> smth.name and disciplines.avgMark is not null "
        "and (smth.name and disciplines.name) in"
        "(select name from marks join disciplines on marks.disciplines_id = disciplines.disciplines_id group by name having count(marks.disciplines_id) > 99)"
        "and disciplines.name in"
        "(select name from marks join disciplines on marks.disciplines_id = disciplines.disciplines_id group by name having count(marks.disciplines_id) > 99)",
        [i,

         ]
        )
    conn.commit()
    i += 1

# conn.commit()
