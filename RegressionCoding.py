# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:40:12 2021

@author: rivas
"""

"""""""""""
Regression
"""""""""""

from sklearn.datasets import load_boston


Boston_P = load_boston()

x = Boston_P.data
y = Boston_P.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, t_test = train_test_split(x,y,test_size = 0.25, train_size = 0.75,
                                                    random_state = 76)

#Normalization
from sklearn.preprocessing import MinMaxScaler
Sc = MinMaxScaler(feature_range = (0, 1))

X_train = Sc.fit_transform(X_train)
X_test = Sc.fit_transform(X_test)

#We need to reshape y_train
y_train = y_train.reshape(-1, 1)
y_train = Sc.fit_transform(y_train)


"""""""""""
MLR
"""""""""""

from sklearn.linear_model import LinearRegression

Linear_R = LinearRegression()

Linear_R.fit(X_train, y_train)

Predicted_values_MLR = Linear_R.predict(X_test)

#DeNormalization
Predicted_values_MLR = Sc.inverse_transform(Predicted_values_MLR)




