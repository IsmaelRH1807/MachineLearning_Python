# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:15:59 2021

@author: rivas
"""

import pandas as pd

Data_Set1 = pd.read_csv('Data_Set1.csv')

Data_test = pd.read_csv('D:\PythonDevelopment\DS_ML_Course\Data_Set1.csv')


#Define a row as the header of the dataset
Data_Set2 = pd.read_csv('Data_Set1.csv', header = 2)

#Rename a column
Data_Set3 = Data_Set2.rename(columns = {'Temperature':'Temp'})

#Remove a column
Data_Set4 = Data_Set3.drop('No. Occupants', axis = 1)

#Save changes in the same dataset (inplace)
Data_Set3.drop('No. Occupants', axis = 1, inplace = True)

#Remove a repeated row
Data_Set5 = Data_Set4.drop(2, axis = 0)

#Reset indexes of the dataset
Data_Set6 = Data_Set5.reset_index(drop=True)

Data_Set6.describe()

#Look for the minimum value of a column and replace it
Min_item = Data_Set6['E_Heat'].min()

Data_Set6['E_Heat'][Data_Set6['E_Heat'] == Min_item] 

Data_Set6['E_Heat'].replace(-4,21, inplace = True)

#Covariance 
Data_Set6.cov()

#Covariance graph with seaborn
#import seaborn as sn

#sn.heatmap(Data_Set6.corr())

""""""""""""
"Missing Values"
""""""""""""

Data_Set6.info()

import numpy as np

#Replace wrong values 
Data_Set7 = Data_Set6.replace('!', np.NaN)

Data_Set7.info()

#Convert categorical values into numbers
Data_Set7 = Data_Set7.apply(pd.to_numeric)

#Search nulls (or empties)
Data_Set7.isnull()

Data_Set7.drop(13, axis = 0, inplace = True)

#Drop all the rows with an NaN
Data_Set7.dropna(axis=0, inplace = True)

#Fill mising values with the last value
Data_Set8 = Data_Set7.fillna(method = 'ffill')

#Fill mising values with the next value
Data_Set8 = Data_Set7.fillna(method = 'bfill')

#Replace missing values with the mean
from sklearn.impute import SimpleImputer 
M_Var = SimpleImputer(missing_values = np.nan, strategy = 'mean')

Data_Set10 = M_Var.fit(Data_Set7)

Data_Set9 = M_Var.transform(Data_Set7)


""""""""""""
"Outlier Detection"
""""""""""""
Data_Set8.boxplot()
#Extract the quantile 1 of E_Plug column
Data_Set8['E_Plug'].quantile(0.25)

#Extract the quantile 3 of E_Plug column
Data_Set8['E_Plug'].quantile(0.75)


# Q1 = 21.25
# Q3 = 33.75

# IQR = Q3 - Q1 = 33.75 - 21.25 = 12.5

# Milt Outlier
# Lower Bound = Q1 - 1.5*IQR = 21.25 - 1.5*12.5
# Upper Bound = Q3 + 1.5*IQR = 33.75 + 1.5*12.5

#Extreme Outlier
# Lower Bound = Q1 - 3*IQR = 21.25 - 3*12.5
# Upper Bound = Q3 + 3*IQR = 33.75 + 3*12.5


Data_Set8['E_Plug'].replace(120, 42, inplace = True)


"""""""""
Concatenation
"""""""""

New_Col = pd.read_csv('Data_New.csv')
#I need a list of dataset for concat, axis 1 for columns, axis 2 for add tuples (rows)
Data_Set10 = pd.concat([Data_Set8, New_Col], axis = 1)


""""""""""""""""""
"""Dummy Variables""
"""""""""""""""
Data_Set10.info()

Data_Set11 = pd.get_dummies(Data_Set10)

Data_Set11.info()


"""""""""
Normalization
"""""""""
from sklearn.preprocessing import minmax_scale, normalize

#First Method:Min Max Scale
Data_Set12 = minmax_scale(Data_Set11,feature_range=(0, 1))
#Second Method, axis 0 for normalizing features / axis 1  for normalizing each sample
Data_Set13 = normalize(Data_Set11, norm = 'l2', axis = 0)

Data_Set13 = pd.DataFrame(Data_Set13, columns = ['Time', 'E_Plug', 'E_Heat', 'Price', 'Temp', 'OffPeak', 'Peak'])













