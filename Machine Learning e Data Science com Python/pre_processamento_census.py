# -*- coding: utf-8 -*-

import pandas as pd 

base = pd.read_csv('census.csv')

previsores = base.iloc[:,0:14].values
classe = base.iloc[:,14].values

# Transformando atributos nominais em atributos discretos
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Variaveis Dummy
column_tranformer = ColumnTransformer([('one_hot_encoder', OneHotEncoder(),
 [1, 3, 5, 6, 7, 8, 9, 13])],remainder='passthrough')
previsores = column_tranformer.fit_transform(previsores).toarray()

labelencorder_classe = LabelEncoder()
classe = labelencorder_classe.fit_transform(classe)

# Escalonamento de valores:
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)