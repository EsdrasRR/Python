# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# Realizando leitura do DataFrame
base = pd.read_csv('credit_data.csv')

# Informaçoes e estatisticas sobre a base
base.describe()

base.loc[base['age'] < 0]

#
## Tratando valores inconsistentes
#
# Apagar a coluna
base.drop('age', 1, inplace=True)

# Apagar somente registros com problemas
base.drop(base[base.age < 0].index, inplace=True)

# Preencher os valores manualmente
# Preencher os valores com a média
base.mean() 
base['age'].mean()
base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = 40.92

#
## Tratando valores faltantes
#
# Buscando valores nulos
pd.isnull(base['age'])
base.loc[pd.isnull(base['age'])]

# Pega do atributo 1 até o 3, o 4 é o maximo superior, ele nao entra
previsores = base.iloc[:,1:4].values
classe = base.iloc[:,4].values

# Atribuindo aos valores faltantes o valor da média dos valores da mesma coluna
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])













