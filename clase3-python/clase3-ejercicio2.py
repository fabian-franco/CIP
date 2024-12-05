import pandas as pd
import numpy as np
import plotly.express as px

football_dic = {
    "player": ["Messi", "Ronaldo", "Neymar", "Mbappe", "Haaland"],
    "year": [2021, 2021, 2021, 2021, 2021],
    "goals": [30, 28, 25, 24, 23]
}

data = pd.DataFrame(football_dic)
print(data)


# Leer un archivo read_csv 
data2 = pd.read_csv("updated_pollution_dataset.csv")
print(data2.head())    
print(data2.tail())
print(data2.shape)
print(data2.size)
print(data2.info())
print(data2.describe())

print(data2.columns)

# cambiar el nombre de las columnas
data2.columns = ['Tempera', 'Humidity', 'PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'Proximity_to_Industrial_Areas', 'Population_Density', 'Air Quality']

print(data2.info())

# Imprimir la columna Temperatura
print(data2['Tempera'])

# Imprimir la columna Temperatura con valores unicos
print(data2['Tempera'].unique())

# Imprimir la columna Temperatura y contar los valores
print(data2['Tempera'].count())

# Imprimir la columna Temperatura con valores unicos y contar los valores
print(data2['Tempera'].value_counts())

# orgenar los valores de la columna Temperatura
print(data2['Tempera'].sort_values())