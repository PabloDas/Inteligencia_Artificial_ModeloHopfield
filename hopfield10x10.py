# INTELIGENCIA ARTIFICIAL - Alumno: Pablo M. Daszczynski
# Red de Hopfield
# Programa adaptado, extendido y corregido del libro
# "García Serrano, A. , (2016), Inteligencia Artificial. Fundamentos, práctica y aplicaciones"

# convertir la cadena de caracteres a valores manejables
def graf_a_valores(datos):
    datos = datos.replace(' ', '')  # quitar espacios
    salida = []
    for i in range(len(datos)):
        if datos[i] == '.':
            salida.append(-1.0)
        else:
            salida.append(1.0)
    return salida


# transformar valores -1 y +1 a representación gráfica
def valores_a_graf(datos):
    salida = ''
    cont = 0
    for i in datos:
        cont = cont + 1
        if i == -1.0:
            salida = salida + '.'
        else:
            salida = salida + 'x'
        if cont % 10 == 0:
            salida = salida + '\n'  # salto de línea
    return salida


# calcula diferencial de energía
def denergia(linea):
    global n_entradas, pesos, nodos_entrada, sum_lin_pesos
    temp = 0.0
    for i in range(n_entradas):
        temp = temp + (pesos[linea][i]) * (nodos_entrada[i])
    return 2.0 * temp - sum_lin_pesos[linea]


# devuelve el valor -1 o 1
def discretizar(n):
    if n < 0.0:
        return -1.0
    else:
        return 1.0


# entrenamiento de la red
def entrenar(datos_ent):
    global n_entradas, pesos, nodos_entrada, sum_lin_pesos
    # actualizamos pesos
    for i in range(1, n_entradas):
        for j in range(i):
            for k in range(len(datos_ent)):
                datos = datos_ent[k]
                t = discretizar(datos[i]) * discretizar(datos[j])
                temp = float(int(t + pesos[i][j]))  # truncar decimales
                pesos[i][j] = temp
                pesos[j][i] = temp  # es una matriz simetrica

    # actualizamos suma de las líneas de la matriz de pesos
    for i in range(n_entradas):
        sum_lin_pesos[i] = 0.0
        for j in range(i):
            sum_lin_pesos[i] = sum_lin_pesos[i] + pesos[i][j]


# clasificar patrón de entrada
def clasificar(patron, iteraciones):
    global n_entradas, pesos, nodos_entrada, sum_lin_pesos
    nodos_entrada = patron[:]
    for i in range(iteraciones):
        for j in range(n_entradas):
            if denergia(j) > 0.0:
                nodos_entrada[j] = 1.0
            else:
                nodos_entrada[j] = -1.0
    return nodos_entrada


if __name__ == '__main__':
    datos_ent = [
        graf_a_valores('.......... \
                        .......... \
                        ....xx.... \
                        ...xxxx... \
                        ..xx..xx.. \
                        ..xx..xx.. \
                        ...xxxx... \
                        ....xx.... \
                        x......... \
                        xx........'),
        graf_a_valores('.......... \
                        .......... \
                        ......xx.. \
                        .....xxxx. \
                        ....xx..xx \
                        ....xx..xx \
                        .....xxxx. \
                        ......xx.. \
                        x......... \
                        xx........'),
        graf_a_valores('.......... \
                        .......... \
                        ....xx.... \
                        ...xxxx... \
                        ..xx..xx.. \
                        ..xx..xx.. \
                        ...xxxx... \
                        ....xx.... \
                        x......... \
                        xx........'),
        graf_a_valores('.......... \
                        .......... \
                        ....xx.... \
                        ...xxxx... \
                        ..xx..xx.. \
                        ..xx..xx.. \
                        ...xxxx... \
                        ....xx.... \
                        x......... \
                        xx........'),

    ]
    n_entradas = 100  # número nodos en la red
    nodos_entrada = [0.0] * n_entradas
    sum_lin_pesos = [0.0] * n_entradas
    # crear matriz de pesos
    pesos = []
    for id in range(n_entradas):
        pesos.append([0.0] * n_entradas)

    entrenar(datos_ent)

    # imprimo matriz de pesos
    print('Matriz de pesos calculada según los datos de entrenamiento:')
    for fila in range(10):
        for columna in range(10):
            print(pesos[fila][columna], end=" ")
        print()
    print()

    # intentar reconocer el carácter distorsionado
    imagen_leida = graf_a_valores('..x....x.. \
                                   xx......x. \
                                   ....xx.... \
                                   x..xxxx... \
                                   ..xx..xx.. \
                                   ..xx..xx.. \
                                   ...xxxx... \
                                   ....xx.... \
                                   x......x.. \
                                   xx......x.')

    reconocida = clasificar(imagen_leida, 5)

print('Caracter introducido:')
print(valores_a_graf(imagen_leida))
print('Caracter reconocido:')
print(valores_a_graf(reconocida))

