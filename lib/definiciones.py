from random import shuffle, randint
from colorama import Fore, Style, Back

ojo = "O" + Style.RESET_ALL
cruz = "┼" + Style.RESET_ALL
vacio = " " + Style.RESET_ALL
espada = "║" + Style.RESET_ALL
luzOn = Fore.YELLOW + "§" + Style.RESET_ALL
luzOff = Style.DIM + "§" + Style.RESET_ALL
goblin = Fore.GREEN + "3" + Style.RESET_ALL
zombie = Fore.CYAN + "4" + Style.RESET_ALL
monstruo = Fore.RED + "5" + Style.RESET_ALL
ciclope = Fore.MAGENTA + "6" + Style.RESET_ALL
escalera = Style.DIM + "≡" + Style.RESET_ALL
corona = Fore.YELLOW + "*" + Style.RESET_ALL
tesoro = Fore.GREEN + "$" + Style.RESET_ALL
tesoroOjo = Fore.RED + "$" + Style.RESET_ALL

desconocida1 = (goblin, ojo)
desconocida2 = (zombie, ciclope)
desconocida3 = (goblin, tesoroOjo)
desconocida4 = (tesoroOjo, zombie)
habitaciones =  [ (ciclope, ciclope), (ojo, tesoro), desconocida1 ]
habitaciones += [ (goblin, ciclope), desconocida2, (tesoro, monstruo) ]
habitaciones += [ (tesoro, ojo), (goblin, goblin), (monstruo, monstruo) ]
habitaciones += [ desconocida3, desconocida4, (zombie, goblin) ]
habitaciones += [ (goblin, goblin), (tesoro, zombie), (tesoroOjo, tesoro) ]
habitaciones += [ (ciclope, tesoro), (ojo, ojo), (tesoro, monstruo) ]
habitaciones += [ (goblin, goblin), (tesoro, tesoroOjo) ]
for i, elemento in enumerate(habitaciones):
    if randint(0, 1):
        habitaciones[i] = elemento[1], elemento[0]
shuffle(habitaciones)

calabozo = []
for _ in range(5): calabozo.append([None] * 5)
calabozo[0][0] = (luzOn, luzOff)
calabozo[0][4] = (luzOn, luzOff)
calabozo[4][0] = (luzOn, luzOff)
calabozo[4][4] = (luzOn, luzOff)
calabozo[2][2] = (escalera, corona)
for i, fila in enumerate(calabozo):
    for j, elemento in enumerate(fila):
        if elemento == None:
            calabozo[i][j] = habitaciones.pop()

combate = [ [(6, ojo), (3, 2)], [(4, 1), (5, ojo)] ]

tesoros  = [1] * 2 + [2] * 2 + [3] * 2 + ["Pocion"] * 3 + [espada] * 3
tesoros += ["Trampa"] * 3 + [ojo] * 3 + [cruz] * 4
shuffle(tesoros)
