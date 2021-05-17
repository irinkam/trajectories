import os
import mysql.connector
import pandas as pd

filepath = "C:\\Users\\lavol\\Desktop\Диплом\\disciplines.csv"
data = pd.read_csv(filepath, delimiter=';', encoding='utf-8')

df = pd.DataFrame(data, columns=['number', 'name', 'avgMark'])

list_of_disciplines = []
list_of_avgmark = []

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

for x in list_of_disciplines: print(x)
for x in list_of_avgmark: print(x)
print()