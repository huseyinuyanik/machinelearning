# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:55:57 2022

@author: hsyn_
"""

#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# veri kümesi
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# eğitim ve test kümelerinin bölünmesi
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Ölçekleme
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# SVM
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)

# Tahminler
y_pred = classifier.predict(X_test)

#  Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print(cm)


#k-katlamali capraz dogrulama 
from sklearn.model_selection import cross_val_score
''' 
1. estimator : classifier (bizim durum)
2. X
3. Y
4. cv : kaç katlamalı

'''
basari = cross_val_score(estimator = classifier, X=X_train, y=y_train , cv = 4) # test train oranımız 4e1 oldugu icin cv 4 secildi

print(basari.mean())            #mean basarıların ortalamasıdır. cv 4 secildigi icin 4 kere test train yer degisti

print(basari.std())             #std standard sapmayı verir. Ne kadar dusukse o kdar iyi.


#**************GridSearch******************

from sklearn.model_selection import GridSearchCV   #parametreler optimize edilecek


p= [{"C":[1,2,3,4,5],
     "kernel":["linear"]},
    {"C":[1,10,100,1000],
     "kernel":["rbf"],"gamma":[1,0.5,0.1,0.05,0.001]}]
    

gs=GridSearchCV(estimator=classifier,   #SVM optimize edilsin
                param_grid=p,           #P degerlerini denesin
                scoring="accuracy",     #Accuracyi score alsın
                cv=10,                  #10 katmanlı
                n_jobs=-1)    


grid_search=gs.fit(X_train,y_train)
eniyisonuc=grid_search.best_score_      # En iyi sonucu dondurur
eniyiparametreler=grid_search.best_params_
print("after GridSearch")
print(eniyisonuc)
print(eniyiparametreler)




"""
GSCV parametreleri
estimator neyi optimize etmek istedigimiz
param_grid: parametreler/denenecekler
scoring   neye göre scorlanacak accuracy gibi
cv: kaç katmanlı olacak
n_jobs: aynı anda çalışacak iş



"""







