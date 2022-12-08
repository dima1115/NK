import pandas as pd
fname='weight.csv'
df=pd.read_csv(fname, sep=';',encoding='cp1251')

df2=pd.DataFrame({'Tv':df.loc[:,'Tv'],
    'Mpv':df.loc[:,'Vp']*df.loc[:,'Cr']})
df2.to_csv('auto.csv', index=False,sep=';',encoding='cp1251')
print(df.loc[:,'Vp']*df.loc[:,'Cr'])


