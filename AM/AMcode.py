import pandas as pd
import os

df = pd.read_csv(r'AM.csv')

pd.set_option('display.max_rows', None)

df.fillna(0)
def replaceLetter(letter):
    df['recurso'] = df['recurso'].replace(letter, 0)
    df['nota'] = df['nota'].replace(letter, 0)
replaceLetter('A')
replaceLetter('D')
replaceLetter('R')
df.to_csv('sortedAM.csv', index= False)

df = pd.read_csv(r'sortedAM.csv')
df_sorted_recurso = df.sort_values(by=['recurso'], ascending=False)
df_sorted_nota = df.sort_values(by=['nota'], ascending=False)

sorted_recurso = df_sorted_recurso.loc[df['curso'] == "LEEC"]
sorted_recurso.reset_index(inplace = True)

sorted_nota = df_sorted_nota.loc[df['curso'] == "LEEC"]
sorted_nota.reset_index(inplace = True)

print(sorted_recurso)

sorted_recurso.to_csv('sorted_recurso_AM.csv', index= False)
sorted_nota.to_csv('sorted_nota_AM.csv', index= False)
