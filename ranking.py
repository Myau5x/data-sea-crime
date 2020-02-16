import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rank_counting(df,crime_cats, imp_times):
    """
    df should contain column Neighborhood
    function calculate number
    groupby Neighborhood, Beat.


    """
    base = df.groupby(by = ['Neighborhood','Beat']).agg('count')['Sector']
    base_agg = base.groupby(level = 0).agg(['min','sum','count'])
    base_num = base_agg.apply(lambda x: x['sum'] if x['count']==1 else (x['sum']-x['min'])/(x['count']-1),axis =1)

    ##count add category
    return base_num + cat_num

df = pd.read_csv('Crime_Data_Cl')

df.index=pd.to_datetime(df['Oc_date'])

df_last = df['2019-01-01':]
df_prev = df['2018-01-01':'2018-12-31']
CAT_ST = []
CAT_FAM = []
CAT_EL = []
tim_st = ()
tim_fam = ()
tim_el = ()

rank_st = 0.9*rank_counting(df_last,CAT_ST,time_st)+0.1*rank_counting(df_prev,CAT_ST,tim_st)
rank_fam = 0.9*rank_counting(df_last,CAT_FAM,tim_fam)+0.1*rank_counting(df_prev,CAT_FAM,tim_fam)
rank_el = 0.9*rank_counting(df_last,CAT_EL,tim_el)+0.1*rank_counting(df_prev,CAT_EL,tim_el)
