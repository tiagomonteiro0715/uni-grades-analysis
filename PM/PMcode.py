import pandas as pd
import os
import numpy as np

df = pd.read_csv(r'PM.csv')

pd.set_option('display.max_rows', None)

def replaceLetter(letter):
    df['lab'] = df['lab'].replace(letter, 0)
    df['nota'] = df['nota'].replace(letter, 0)
replaceLetter('A')
replaceLetter('D')
replaceLetter('R')
replaceLetter('NE')
replaceLetter('RP')

df['1_teste'] = df['1_teste'].replace('nan', np.nan).fillna(0)
df['2_teste'] = df['2_teste'].replace('nan', np.nan).fillna(0)
df['3_teste'] = df['3_teste'].replace('nan', np.nan).fillna(0)
df['exame'] = df['exame'].replace('nan', np.nan).fillna(0)
df['media'] = df['media'].replace('nan', np.nan).fillna(0)
df['lab'] = df['lab'].replace('nan', np.nan).fillna(0)
df['nota'] = df['nota'].replace('nan', np.nan).fillna(0)
del df["1_teste"]
del df["2_teste"]
del df["3_teste"]

df.to_csv('sortedPM.csv', index= False)

df = pd.read_csv(r'sortedPM.csv')


    
    
    
df_sorted_nota = df.sort_values(by=['nota'], ascending=False)


df_sorted_nota.to_csv('sorted_nota_PM.csv', index= False)