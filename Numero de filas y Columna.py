# Número de filas y columnas de la sala de cine
NUM_FILAS = 3
NUM_COLUMNAS = 4

# Crear la matriz "asientos" como una lista de listas, inicializada en 0
# (0 = libre). Se construye con comprensión de listas para evitar que
# todas las filas apunten a la misma lista en memoria.
asientos = [[0 for columna in range(NUM_COLUMNAS)] for fila in range(NUM_FILAS)]

# Solicitar al usuario la fila y la columna del asiento a reservar,
# validando que los valores ingresados estén dentro del rango permitido.
fila_valida = False
while not fila_valida:
    fila = int(input(f"Ingrese fila (0 a {NUM_FILAS - 1}): "))
    if 0 <= fila < NUM_FILAS:
        fila_valida = True
    else:
        print("Fila fuera de rango. Intente nuevamente.")

columna_valida = False
while not columna_valida:
    columna = int(input(f"Ingrese columna (0 a {NUM_COLUMNAS - 1}): "))
    if 0 <= columna < NUM_COLUMNAS:
        columna_valida = True
    else:
        print("Columna fuera de rango. Intente nuevamente.")

# Verificar si el asiento ya estaba reservado antes de marcarlo
if asientos[fila][columna] == 1:
    print("Aviso: ese asiento ya estaba reservado.")
else:
    # Marcar el asiento seleccionado como reservado (1)
    asientos[fila][columna] = 1
    print("Asiento reservado con éxito.")

# Mostrar el estado completo de la sala recorriendo la matriz
# con dos bucles anidados: uno para las filas y otro para las columnas.
print("\nEstado de la sala:")
for i in range(NUM_FILAS):
    for j in range(NUM_COLUMNAS):
        print(asientos[i][j], end=" ")
    print()