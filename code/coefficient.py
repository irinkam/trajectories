import os
import pandas as pd
import csv

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\files\\disciplines.csv"
data = pd.read_csv(filepath, delimiter=';', encoding='utf-8')

df_1 = pd.DataFrame(data, columns=['number', 'name', 'avgMark'])
df_2 = df_1

list_of_disciplines_1 = []
list_of_disciplines_2 = []
list_of_disciplines_final = []

coefficient = 0
i = 0

for row_1 in df_1.itertuples():
    for row_2 in df_2.itertuples():
        if row_1.name == row_2.name: continue
        coefficient = row_1.avgMark / row_2.avgMark
        if coefficient > 1: coefficient = 1 / coefficient
        list_of_disciplines_final.append([row_1.name, row_2.name, coefficient])
    df_2 = df_2.drop(i)
    i += 1

# for x in list_of_disciplines_final: print(x)

# print(len(list_of_disciplines_final))
# print(len(df_1))

# with open("C:\\Users\\lavol\\Desktop\\Диплом\\filename.csv", 'w') as coefficient_of_disciplines:
#     wr = csv.writer(coefficient_of_disciplines, quoting=csv.QUOTE_ALL)
#     wr.writerow(list_of_disciplines_final)