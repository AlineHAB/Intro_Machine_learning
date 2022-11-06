# -*- coding: utf-8 -*-
"""ATV1_2ML_ALine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w_0NqtsEBh0KUtL1s4PJlC9jS5BIljM-
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('/content/car_data.csv')
df.head()

df['tipo_transmissao'].replace({'Manual': 0, 'Automatico': 1}, inplace=True)
df['tipo_vendedor'].replace({'Revendedor': 0, 'Individual': 1}, inplace=True)
df['tipo_combustivel'].replace({'Gasolina': 0, 'Diesel': 1, 'GasNatural': 2}, inplace=True)
df.head()

plt.scatter(df['ano'], df['preco_venda'],  color='pink')
plt.xlabel("Ano do Carro")
plt.ylabel("Preço de venda")
plt.show()

plt.scatter(df['ano'], df['kms_rodados'],  color='red')
plt.xlabel("Ano do Carro")
plt.ylabel("Kms Rodados")
plt.show()

"""NOVAS VARIAVEIS"""

new_x = df[['ano', 'preco_atual', 'kms_rodados', 'tipo_combustivel']]
new_y = df[['preco_venda']]

"""SEPARANDO EM TRINO E TESTE"""

from sklearn.model_selection import train_test_split
new_x_train, new_x_test, new_y_train, new_y_test = train_test_split(new_x, new_y, test_size=0.2)

print('TREINO')
print("new_x_train: ", new_x_train.shape)
print("new_y_train: ", new_y_train.shape)

print('\nTESTE')
print("new_x_test: ", new_x_test.shape)
print("new_y_test: ", new_y_test.shape)

"""TREINANDO O MODELO"""

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(new_x_train, new_y_train)

y_prediction = model.predict(new_x_test)

print(y_prediction.shape)
print(new_y_test.shape)

plt.plot(range(y_prediction.shape[0]), y_prediction, 'b--')
plt.plot(range(new_y_test.shape[0]), new_y_test, 'g--')
plt.legend(['Preço previsto', 'Preço real'])
plt.ylabel('Preço')
plt.xlabel('Indice')
plt.show()

"""USANDO A MEDIDA R2"""

from sklearn.metrics import r2_score
print('R2 - SCORE: ', r2_score(new_y_test, y_prediction))