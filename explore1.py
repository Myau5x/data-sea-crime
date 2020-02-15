import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Crime_Data.csv')
df.dropna(inplace= True)
df['Oc_date'] = pd.to_datetime(df['Occurred Date'])
NEW_COL = ['Oc_date', 'Occurred Time',
       'Crime Subcategory', 'Primary Offense Description', 'Precinct',
       'Sector', 'Beat', 'Neighborhood']

new_df = df[NEW_COL][df['Oc_date']>='01/01/2008']
new_df = new_df[new_df['Neighborhood']!='UNKNOWN']
new_df.to_csv('Crime_Data_Cl',index=False)
