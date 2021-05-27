import os
import pandas as pd

#filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\files\\disciplines.csv"
filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\files\\disciplines_1.csv"
#filepath = "C:\\Users\\lavol\\Desktop\\Диплом\\disciplines_1.csv"
data = pd.read_csv(filepath, delimiter=';', encoding='utf-8')

df_1 = pd.DataFrame(data, columns=['number', 'name', 'avgMark'])
df_2 = df_1

list_of_disciplines_final = []
coefficient = 0
i = 0
k = 0

for row_1 in df_1.itertuples():
    for row_2 in df_2.itertuples():
        if row_1.name == row_2.name: continue
        coefficient = row_1.avgMark / row_2.avgMark
        if coefficient > 1: coefficient = 1 / coefficient
        list_of_disciplines_final.append([row_1.name, row_2.name, coefficient])
        # df_2.drop()
        k += 1
    # df_1.drop()
    i += 1

for x in list_of_disciplines_final: print(x)
