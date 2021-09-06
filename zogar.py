from lib.definiciones import *

def manejarOjo(inventario):
    global spots

    if cruz not in inventario:
        spots -= 1
    else:
        inventario.remove(cruz)

def manejarHabitacion(habitacion, inventario):
    global corazones, puntos, nivel

    if habitacion[0] in [ojo, tesoroOjo]:
        manejarOjo(inventario)
    if habitacion[0] in [tesoro, tesoroOjo] and tesoros:
        premio = tesoros.pop()
        if premio in [1, 2, 3]:
            puntos += premio
        elif premio == ojo:
            manejarOjo(inventario)
        elif premio == "Trampa":
            corazones -= 1
        elif premio == "Pocion":
            corazones += 1 if corazones < 15 else 0
        else:
            inventario += [premio]
    elif habitacion[0] == corona:
        puntos += 10
        inventario += [corona]
        for i, fila in enumerate(calabozo):
            for j, elemento in enumerate(fila):
                if elemento[0] == corona:
                    calabozo[i][j] = (vacio, escalera)
    elif habitacion[0] in [goblin, zombie, monstruo, ciclope]:
        manejarEnemigo(int(habitacion[0][5]))
    elif habitacion[0] == escalera and corona in inventario:
        nivel = 4

def voltear(matriz, posicion):
    i, j = posicion
    matriz[i][j] = matriz[i][j][1], matriz[i][j][0]

def manejarEnemigo(vida):
    global daño, corazones

    while vida > 0 and corazones > 0:
        mostrarMenu()
        print(f"\nVida enemigo: {vida}.")

        voltear(combate, daño)
        daño = moverJugador(daño)
        i, j = daño

        if combate[i][j][0] == ojo:
            manejarOjo(inventario)
        else:
            vida -= combate[i][j][0]

        for elemento in inventario:
            if elemento == espada and vida > 0:
                if input("Desea usar una espada? (S/N): ") != "N":
                    inventario.remove(espada)
                    vida -= 1

        if vida > 0: corazones -= 1

def imprimirTablero(tablero, posicion):
    for i, fila in enumerate(tablero):
        for j, elemento in enumerate(fila):
            if (i, j) == posicion: print(Back.YELLOW, end = "")
            print(elemento[0], end = Style.RESET_ALL + " ")
        print("")

def mostrarMenu():
    global daño, jugador

    for _ in range(100): print("")
    imprimirTablero(combate, daño)
    print(f"\nPuntos: {puntos}.")
    print(f"Spots: {spots}.")
    print(f"Corazones: {corazones}.")
    print(f"Inventario:", end = " ")
    for elemento in inventario:
        print(elemento, end = ", ")
    print("\n")
    imprimirTablero(calabozo, jugador)

def moverJugador(posicion):
    print("\n8 - Arriba.")
    print("4 - Izquierda.")
    print("6 - Derecha.")
    print("2 - Abajo.")
    movimiento = int(input("Ingrese movimiento: "))

    if   movimiento == 8: posicion = posicion[0] - 1, posicion[1]
    elif movimiento == 2: posicion = posicion[0] + 1, posicion[1]
    elif movimiento == 4: posicion = posicion[0], posicion[1] - 1
    elif movimiento == 6: posicion = posicion[0], posicion[1] + 1

    return posicion

def voltearEscalera():
    for i, fila in enumerate(calabozo):
        for j, elemento in enumerate(fila):
            if escalera in elemento:
                voltear(calabozo, (i, j))

def cambiarHabitacion(antes, ahora):
    global nivel

    i, j = ahora
    if calabozo[i][j][0] in [luzOn, luzOff]:
        voltear(calabozo, ahora)

    luces = 0
    for fila in calabozo:
        for elemento in fila:
            if luzOn in elemento[0]: luces += 1

    if nivel in [1, 3]:
        i, j = antes
        if luces == 0:
            if nivel == 1: nivel = 2
            voltearEscalera()
    elif nivel == 2:
        i, j = ahora
        if luces == 4:
            nivel = 3
            voltearEscalera()

    habitacion = calabozo[i][j][0]
    if habitacion not in [luzOn, luzOff, vacio, corona, escalera]:
        voltear(calabozo, (i, j))

nivel = 1
spots = 14
corazones = 15
jugador = 2, 2
daño = 0, 1
puntos = 0
inventario = []

while corazones > 0 and spots > 0 and nivel < 4:
    i, j = jugador
    manejarHabitacion(calabozo[i][j], inventario)
    mostrarMenu()
    if corazones > 0 and spots > 0 and nivel < 4:
        jugador = moverJugador(jugador)
        cambiarHabitacion((i, j), jugador)

print("\nFin del juego.")
