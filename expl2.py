import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def goodname(name):
    r = name.replace(' ','_')
    r = r.replace('/','_')
    return r

df = pd.read_csv('Crime_Data_Cl')

df.index=pd.to_datetime(df['Oc_date'])
NEI = df.Neighborhood.unique()
for neigh in NEI:
    plt.figure()
    df_nei = df[df.Neighborhood==neigh]
    df_ngr = df_nei.groupby(by = pd.Grouper(freq='M')).agg('count')
    y = df_ngr['Beat']
    x = df_ngr.index
    plt.plot(x,y)
    plt.xlabel('Month')
    plt.ylabel('Crime')
    plt.savefig('pics/{0}.jpg'.format(goodname(neigh)))
    plt.close()
