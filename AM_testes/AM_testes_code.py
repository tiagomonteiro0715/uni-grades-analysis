import pandas as pd
import os

df = pd.read_csv(r'AM-file.csv')

pd.set_option('display.max_rows', None)
num_collums = ['MT1','MT2','MT3','Teste_1','Teste_2','Nota_Final']

def replaceLetter(letter):
    df['Nota_Final'] = df['Nota_Final'].replace(letter, 0)

for i in len(num_collums):
    if num_collums[i] == 'A':
        replaceLetter('A')





df = df.loc[df['freq'] == "S"]

#df_sorted_Nota_Final = df.sort_values(by=['Nota_Final'], ascending=False)
#df_sorted_2teste = df.sort_values(by=['Teste_2'], ascending=False)

#df = df.loc[df['curso'] == "LEEC"]# - ver da universidade toda.
#df = df.loc[df['Nota_Final'] == 10]

print(df.head(1000))

'''

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
'''