import os
import mysql.connector
import pandas as pd

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\files\\disciplines.csv"
data = pd.read_csv(filepath, delimiter=';', encoding='utf-8')

df = pd.DataFrame(data, columns=['number', 'name', 'avgMark'])

list_of_disciplines = []
list_of_avgmark = []
list_of_disciplines_distinct = []
list_of_avgmark_distinct = []

for row in df.itertuples():
    count = 0
    sum = 0
    for char in row.name:
        if char.isdigit():
            n = row.name.index(char)
            g = row.name[:n-1]
            for row in df.itertuples():
                if row.name[:n-1] == g:
                    count += 1
                    sum += float(row.avgMark)
                    ind = df.index
            list_of_disciplines.append(g)
            list_of_avgmark.append(sum / count)
            break
#df.drop_duplicates(subset=['name'])

i = 0
while i < len(list_of_disciplines):
    if not list_of_disciplines[i] in list_of_disciplines_distinct:
        list_of_disciplines_distinct.append(list_of_disciplines[i])
    i += 1

i = 0
while i < len(list_of_avgmark):
    if not list_of_avgmark[i] in list_of_avgmark_distinct:
        list_of_avgmark_distinct.append(list_of_avgmark[i])
    i += 1

for x in list_of_disciplines_distinct: print(x)
for x in list_of_avgmark_distinct: print(x)
print()