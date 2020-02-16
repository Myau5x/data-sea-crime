import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rank_counting(df,CAT, imp_times=(0,2400)):
    """
    df should contain column Neighborhood
    function calculate number
    groupby Neighborhood, Beat.


    """
    base = df.groupby(by = ['Neighborhood','Beat']).agg('count')['Sector']
    base_agg = base.groupby(level = 0).agg(['min','sum','count'])
    base_num = base_agg.apply(lambda x: x['sum'] if x['count']==1 else (x['sum']-x['min'])/(x['count']-1),axis =1)
    s = base_num.sum()
    base_num = base_num/s
    ##count add category
    mask_cat = (df['Crime Subcategory'].isin(CAT))
    day_start = imp_times[0]
    day_fin = imp_times[1]

    mask_ti = (df['Occurred Time']>=day_start)|(df['Occurred Time']<=day_fin)
    df2 = df[mask_cat&mask_ti]
    cat = df2.groupby(by = ['Neighborhood','Beat']).agg('count')['Sector']
    cat_agg = cat.groupby(level = 0).agg(['min','sum','count'])
    cat_num = cat_agg.apply(lambda x: x['sum'] if x['count']==1 else (x['sum']-x['min'])/(x['count']-1),axis =1)
    s =  cat_num.sum()
    cat_num = cat_num/s
    return base_num + cat_num

df = pd.read_csv('Crime_Data_Cl')

df.index=pd.to_datetime(df['Oc_date'])
"""
['BURGLARY-COMMERCIAL', 'TRESPASS', 'CAR PROWL', 'THEFT-BUILDING',
       'DUI', 'AGGRAVATED ASSAULT', 'BURGLARY-RESIDENTIAL-SECURE PARKING',
       'THEFT-ALL OTHER', 'AGGRAVATED ASSAULT-DV', 'THEFT-SHOPLIFT',
       'BURGLARY-RESIDENTIAL', 'THEFT-BICYCLE', 'ROBBERY-RESIDENTIAL',
       'FAMILY OFFENSE-NONVIOLENT', 'MOTOR VEHICLE THEFT', 'WEAPON',
       'NARCOTIC', 'SEX OFFENSE-OTHER', 'RAPE', 'ROBBERY-STREET', 'ARSON',
       'BURGLARY-COMMERCIAL-SECURE PARKING', 'ROBBERY-COMMERCIAL',
       'PROSTITUTION', 'PORNOGRAPHY', 'GAMBLE', 'DISORDERLY CONDUCT',
       'HOMICIDE', 'LIQUOR LAW VIOLATION', 'LOITERING']
"""


df_last = df['2019-01-01':]
df_prev = df['2018-01-01':'2018-12-31']
CAT_ST = ['CAR PROWL']
CAT_FAM = ['ROBBERY-STREET','NARCOTIC','THEFT-ALL OTHER','PORNOGRAPHY']
CAT_EL = ['TRESPASS','ROBBERY-RESIDENTIAL']
# tim_st =
tim_fam = (800,2000)
tim_el = (700,2100)

rank_st = 0.9*rank_counting(df_last,CAT_ST)+0.1*rank_counting(df_prev,CAT_ST)
rank_fam = 0.9*rank_counting(df_last,CAT_FAM,tim_fam)+0.1*rank_counting(df_prev,CAT_FAM,tim_fam)
rank_el = 0.9*rank_counting(df_last,CAT_EL,tim_el)+0.1*rank_counting(df_prev,CAT_EL,tim_el)

##save to to_csv
rank_st.sort_values().to_csv('rank_student.csv')
rank_fam.sort_values().to_csv('rank_family.csv')
rank_el.sort_values().to_csv('rank_elderly.csv')
