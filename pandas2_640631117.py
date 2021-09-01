# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:28:33 2021

@author: Chanwit Chanton

"""
import pandas as pd
df=pd.read_csv("Salaries.csv")

#Quiz1

# Try to read the first 10, 20, 50 records;
#fish head
print(df.head(10))
print(df.head(20))
print(df.head(50))
 # How to view the last few records;
#fish tail as 5 enders
print(df.tail())


#13 Items

# 5beginers
print(df.head())

#Groupby
df_rank = df.groupby(['rank'])
print(df_rank.mean())

print(df.groupby('rank')[['salary']].mean())

print(df.groupby(['rank'], sort=False)[['salary']].mean())

#filtering
df_sub=df[df['salary']>120000]
print(df_sub)

df_f=df[df['sex']=='Female']
print(df_f)

#Slicing
print(df['salary'])

print(df[['rank','salary']])

print(df[10:20])

print(df_sub.loc[10:20,['rank','sex','salary']])

print(df_sub.iloc[10:20,[0,3,4,5]])

#sorting
df_sorted=df.sort_values(by='service')
print(df_sorted.head())

df_sorted=df.sort_values(by=['service','salary'], ascending=[True,False])
print(df_sorted.head(10))