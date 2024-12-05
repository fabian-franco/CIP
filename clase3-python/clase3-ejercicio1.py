import numpy as np

# Crear un array de 5 elementos
array_basico = np.array([1, 2, 3, 4, 5])

# Imprimir el array y el primer elemento
print(array_basico)
print(array_basico[0])

# Modificar el primer elemento
array_basico[0] = 10
print(array_basico)

# multipliccion de un array
print(array_basico * 2)

# minimo, maximo y suma
print(array_basico.min())
print(array_basico.max())
print(array_basico.sum())

# Imprimir desde la posicion 2 en adelante
print(array_basico[2:])

# Imprimir desde la posicion 2 hasta el final
print(array_basico[:2])

# Imprimir desde la posicion 1 hasta la 3
print(array_basico[1:4])

# Cambiar todas las posiciones del array a 0
array_basico[:] = 99
print(array_basico)

# Array multidimencional de 2x4
array_multidimencional = np.array([[1, 2, 3,5], [5, 6, 7, 8]])
print(array_multidimencional)

# Array bidimensional de 3x4
array_bidimensional = np.array([[1, 2, 3, 5], [5, 6, 7, 8], [9, 10, 11, 12]])
print(array_bidimensional)

# Imprimir la primera fila
print(array_bidimensional[0])

# Imprimir una columna
print(array_bidimensional[:, 0])

print(array_bidimensional[:2, 2:])

# minimo, maximo y suma
print(array_bidimensional.min())
print(array_bidimensional.max())
print(array_bidimensional.sum())

# minimo, maximo y suma por columna
print(array_bidimensional.max(axis=1))