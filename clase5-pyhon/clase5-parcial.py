import pandas as pd

df = pd.read_csv("datos.csv")

print("Filas y columnas: ", df.shape)

df.columns = ['Codigo', 'Apellidos', 'Nombres', 'Genero', 'Edad', 'Fecha de Ingreso', 'Puesto', 'Ubicacion', 'Sueldo Base', 'Bonificacion', 'Total']

print("Hombres y mujeres: ", df['Genero'].value_counts())

print("Persona que recibe más dinero: ", df.loc[df['Total'].idxmax()])

import plotly.express as px
fig = px.scatter(df, x='Edad', y='Total', color='Genero')

fig.show()

## Resultados:

# En la gráfica se puede observar que las mujeres tienen un sueldo base mayor que los hombres, sin embargo, los hombres tienen una bonificación mayor que las mujeres.