


import random



def generar_posicion(ocupadas, limite):

    while True:

        x = random.randint(-limite, limite)
        y = random.randint(-limite, limite)
        
        if (x, y) not in ocupadas:
            ocupadas.append((x, y))
            return x, y
        

def comprobar_posicion(
    xJ, yJ,
    objetivo_x, objetivo_y,
    randomObjeto1_x, randomObjeto1_y,
    randomObjeto2_x, randomObjeto2_y,
    randomObjeto3_x, randomObjeto3_y,
    randomObjeto4_x, randomObjeto4_y,
    randomObjeto5_x, randomObjeto5_y,
    energia,
    objetosEncontrados,
    Objeto1, Objeto2, Objeto3, Objeto4, Objeto5
):

    victoria = False

    # Base
    if xJ == objetivo_x and yJ == objetivo_y:
        print("\n¡Has encontrado una antigua base alienígena!")
        print("¡MISIÓN COMPLETADA!")
        victoria = True

    # Objeto 1
    if xJ == randomObjeto1_x and yJ == randomObjeto1_y:
        print("\n¡Has encontrado el objeto alienígena 1!")
        print("¡Energía +200!")
        energia += 200
        print(f"Energía: {energia}")
        objetosEncontrados += 1
        Objeto1 = True
        randomObjeto1_x = None
        randomObjeto1_y = None

    # Objeto 2
    if xJ == randomObjeto2_x and yJ == randomObjeto2_y:
        print("\n¡Has encontrado el objeto alienígena 2!")
        print("¡Energía +100!")
        energia += 100
        print(f"Energía: {energia}")
        objetosEncontrados += 1
        Objeto2 = True
        randomObjeto2_x = None
        randomObjeto2_y = None

    # Objeto 3
    if xJ == randomObjeto3_x and yJ == randomObjeto3_y:
        print("\n¡Has encontrado el objeto alienígena 3!")
        print("¡Energía -10!")
        energia -= 10
        print(f"Energía: {energia}")
        objetosEncontrados += 1
        Objeto3 = True
        randomObjeto3_x = None
        randomObjeto3_y = None

    # Objeto 4
    if xJ == randomObjeto4_x and yJ == randomObjeto4_y:
        print("\n¡Has encontrado el objeto alienígena 4!")
        print("¡Energía -5!")
        energia -= 5
        print(f"Energía: {energia}")
        objetosEncontrados += 1
        Objeto4 = True
        randomObjeto4_x = None
        randomObjeto4_y = None

    # Objeto 5
    if xJ == randomObjeto5_x and yJ == randomObjeto5_y:
        print("\n¡Has encontrado el objeto alienígena 5!")
        print("¡Energía +150!")
        energia += 150
        print(f"Energía: {energia}")
        objetosEncontrados += 1
        Objeto5 = True
        randomObjeto5_x = None
        randomObjeto5_y = None

    return (
        victoria,
        energia,
        objetosEncontrados,
        randomObjeto1_x, randomObjeto1_y,
        randomObjeto2_x, randomObjeto2_y,
        randomObjeto3_x, randomObjeto3_y,
        randomObjeto4_x, randomObjeto4_y,
        randomObjeto5_x, randomObjeto5_y,
        Objeto1, Objeto2, Objeto3, Objeto4, Objeto5
    )
        

def jugar():


    decision = ""

    PrimeraRonda = True

    Objeto1 = False
    Objeto2 = False
    Objeto3 = False
    Objeto4 = False
    Objeto5 = False

    Teletransportado = False
    MisilEnergia = False

    causaFinal = ""
    ResultadoF = ""

    print("\n¡Bienvenido a la expedición espacial!")
    print("En esta aventura, serás un astronauta explorando un planeta desconocido.")
    print("Deberás explorar, investigar y sobrevivir mientras gestionas tu energía y movimientos.")
    print("Hemos oído rumores de que hay vida en dicho planeta, ")
    print("y tu objetivo será explorar el planeta y descubrir si los rumores sobre la existencia de una base alienígena son ciertos.")
    print("A continuación deberás ingresar los datos de la expedición.")

    while True:
        nombreE = input("\nNombre de la expedición: ").strip()
        if nombreE:
            break
        print("Error: Debes introducir un nombre para la expedición.")
    while True:
        nombreP = input("Nombre del planeta: ").strip()
        if nombreP:
            break
        print("Error: Debes introducir un nombre para el planeta.")
    while True:
        nombreJ = input("Nombre del jugador: ").strip()
        if nombreJ:
            break
        print("Error: Debes introducir un nombre para el jugador.")
    #INTRODUCIR LIMITE MAPA
    while True:
        try:
            LIMITE = int(input("Introduce el límite del mapa (mínimo 2): "))
            if LIMITE >= 2:
                break
            else:
                print("Debe ser como mínimo 2.")

        except ValueError:
            print("Introduce un número entero.")


    #INTRODUCIR LIMITE MOVIMIENTOS
    while True:
        try:
            movFinal = int(input("Introduce la cantidad de movimientos (entre 5 y 15): "))
            if movFinal >= 5 and movFinal <= 15:
                break
            else:
                print("Debe estar entre 5 y 15.")

        except ValueError:
            print("Introduce un número entero.")


    while True:
        try:
            xJ = int(input("Posición X inicial: "))
            if xJ < -LIMITE or xJ > LIMITE:
                print(f"La posición X debe estar entre -{LIMITE} y {LIMITE}.")
            else:
                break
            
        except ValueError:
            print("Debes introducir un número entero.")

    while True:
        try:
            yJ = int(input("Posición Y inicial: "))
            if yJ < -LIMITE or yJ > LIMITE:
                print(f"La posición Y debe estar entre -{LIMITE} y {LIMITE}.")
            else:
                break

        except ValueError:
         print("Debes introducir un número entero.")

    
    energia = 100
    
    pistaComprada = False
    

    ocupadas = [(xJ, yJ)]

    objetivo_x, objetivo_y = generar_posicion(ocupadas, LIMITE)

    randomObjeto1_x, randomObjeto1_y = generar_posicion(ocupadas, LIMITE)
    randomObjeto2_x, randomObjeto2_y = generar_posicion(ocupadas, LIMITE)
    randomObjeto3_x, randomObjeto3_y = generar_posicion(ocupadas, LIMITE)
    randomObjeto4_x, randomObjeto4_y = generar_posicion(ocupadas, LIMITE)
    randomObjeto5_x, randomObjeto5_y = generar_posicion(ocupadas, LIMITE)

    objetosEncontrados = 0

    print("\n ==================================================")
    print("       ~ ~ ~ INICIO DE EXPEDICIÓN ~ ~ ~            ")
    print("===================================================")
    print("Expedición:", nombreE)
    print("Planeta:", nombreP)
    print("Jugador:", nombreJ)
    print("Posición inicial:", xJ, yJ)
    print("Energía:", energia)
    print("Movimientos: ", movFinal)
    print("Limite de exploración: ±", LIMITE)

    xInicial = xJ
    yInicial = yJ

    energiaInicial = energia

    movimientosIniciales = movFinal

    print("\n ==================================================")
    print("             ~ ~ ~ CÓMO JUGAR ~ ~ ~                ")
    print("===================================================")
    print(f"El objetivo de la expedición {nombreE} es explorar el planeta {nombreP} y descubrir sus secretos.")
    print("Tendrás que moverte por el planeta, pero ten cuidado con tu energía,")
    print("ya que cada movimiento la consume.")
    print("Si tu energía llega a cero, la expedición habrá fracasado.")
    print(f"Tienes un máximo de {movFinal} movimientos, ya que nuestro oxígeno es limitado, pero puedes canjearlo por energía.")
    print(f"No puedes salir del límite establecido, que sería de ±{LIMITE} en ambos ejes,")
    print("ya que no sabemos qué peligros pueden haber fuera de esa zona.")
    print("Según los rumores, hay una base alienígena en algún lugar del planeta.")
    print("Si consigues encontrarla, habrás completado la misión con éxito.")
    print("Además, hay objetos alienígenas que pueden ayudarte o perjudicarte en tu expedición.")
    print("Según nuestros radares, estos objetos estan ubicados en las siguientes coordenadas:")
    print(f"Objeto 1: ({randomObjeto1_x}, {randomObjeto1_y})")
    print(f"Objeto 2: ({randomObjeto2_x}, {randomObjeto2_y})")
    print(f"Objeto 3: ({randomObjeto3_x}, {randomObjeto3_y})")
    print(f"Objeto 4: ({randomObjeto4_x}, {randomObjeto4_y})")
    print(f"Objeto 5: ({randomObjeto5_x}, {randomObjeto5_y})")

    print(f"\n~ ~ ~ ¡La expedición ha comenzado! ¡Buena suerte, astronauta {nombreJ}! ~ ~ ~")
    movimientos = 0
    
    ronda = 1

    while energia > 0 and movimientos < movFinal:
        
        randomCosa = random.randint(0, 25)
        energia_anterior = energia



        if not PrimeraRonda:
            if randomCosa == 1:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n¡Un misil de energía!")
                print(f"¡Has ganado 500 puntos de energía!")
                print("\n")
                energia += 500
                MisilEnergia = True
                print(f"Energía: {energia}")

            if randomCosa == 13:
                xR= random.randint(-LIMITE, LIMITE)
                yR= random.randint(-LIMITE, LIMITE)
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n¡Los alienígenas te han teletransportado!")
                print(f"¡Te has teletransportado a una nueva ubicación!")
                print("Según nuestros radares, tu nueva posición es:")
                print(f"({xR}, {yR})")
                print("\n")
                Teletransportado = True
                xJ = xR
                yJ = yR

                (
                    victoria,
                    energia,
                    objetosEncontrados,
                    randomObjeto1_x, randomObjeto1_y,
                    randomObjeto2_x, randomObjeto2_y,
                    randomObjeto3_x, randomObjeto3_y,
                    randomObjeto4_x, randomObjeto4_y,
                    randomObjeto5_x, randomObjeto5_y,
                    Objeto1, Objeto2, Objeto3, Objeto4, Objeto5
                ) = comprobar_posicion(
                    xJ, yJ,
                    objetivo_x, objetivo_y,
                    randomObjeto1_x, randomObjeto1_y,
                    randomObjeto2_x, randomObjeto2_y,
                    randomObjeto3_x, randomObjeto3_y,
                    randomObjeto4_x, randomObjeto4_y,
                    randomObjeto5_x, randomObjeto5_y,
                    energia,
                    objetosEncontrados,
                    Objeto1, Objeto2, Objeto3, Objeto4, Objeto5
                )

                if victoria:
                    break




        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n             ~ ~ ~ RONDA {ronda} ~ ~ ~                ")
        print("\n¿Qué deseas hacer? ")
        print("M: Moverte")
        print("C: Comprar movimientos")
        print("P: Pista de la base alienígena")
        print("S: Salir de la expedición")

        decision = input("Inserta tu opción: ").upper()

        x_anterior = xJ
        y_anterior = yJ
        
        if decision == "M":


            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            print("\n¿Dónde quieres ir? ")
            print("N. Norte ↑")
            print("S. Sur ↓")
            print("E. Este →")
            print("O. Oeste ←")
            print("C. Cancelar")

            direccion = input("Inserta tu opción: ").upper()
            if direccion == "N":
                yJ += 1
            elif direccion == "S":
                yJ -= 1
            elif direccion == "E":
                xJ += 1
            elif direccion == "O":
                xJ -= 1
            elif direccion == "C":
                print("Has cancelado el movimiento. ")
                continue
            else:
                print("Dirección no válida.")
                continue
            

            if xJ > LIMITE or xJ < -LIMITE or yJ > LIMITE or yJ < -LIMITE:
                print(f"No puedes salir del límite establecido. (±{LIMITE} en ambos ejes).")
                xJ = x_anterior
                yJ = y_anterior
                continue


            energia -= 10
            movimientos += 1

            (
                victoria,
                energia,
                objetosEncontrados,
                randomObjeto1_x, randomObjeto1_y,
                randomObjeto2_x, randomObjeto2_y,
                randomObjeto3_x, randomObjeto3_y,
                randomObjeto4_x, randomObjeto4_y,
                randomObjeto5_x, randomObjeto5_y,
                Objeto1, Objeto2, Objeto3, Objeto4, Objeto5
            ) = comprobar_posicion(
                xJ, yJ,
                objetivo_x, objetivo_y,
                randomObjeto1_x, randomObjeto1_y,
                randomObjeto2_x, randomObjeto2_y,
                randomObjeto3_x, randomObjeto3_y,
                randomObjeto4_x, randomObjeto4_y,
                randomObjeto5_x, randomObjeto5_y,
                energia,
                objetosEncontrados,
                Objeto1, Objeto2, Objeto3, Objeto4, Objeto5
            )

            if victoria:
                break

        elif decision == "C":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n¿Cuántos movimientos deseas comprar?")
            print(f"Energia: {energia}")
            print("1. 1 movimientos por 5 puntos de energía")
            print("2. 5 movimientos por 20 puntos de energía")
            print("3. 10 movimientos por 45 puntos de energía")
            print("4. Cancelar")

            compra = input("Inserta tu opción: ")

            if compra == "1":
                if energia >= 5:
                    energia -= 5
                    movFinal += 1
                    print("Has comprado 1 movimientos por 5 puntos de energía.")
                else:
                    print("No tienes suficiente energía para comprar esta opción.")

            elif compra == "2":
                if energia >= 20:
                    energia -= 20
                    movFinal += 5
                    print("Has comprado 5 movimientos por 20 puntos de energía.")
                else:
                    print("No tienes suficiente energía para comprar esta opción.")

            elif compra == "3":
                if energia >= 45:
                    energia -= 45
                    movFinal += 10
                    print("Has comprado 10 movimientos por 45 puntos de energía.")
                else:
                    print("No tienes suficiente energía para comprar esta opción.")

            elif compra == "4":
                print("Has cancelado la compra de movimientos.")
                continue

            else:
                print("Opción no válida.")

        elif decision == "P":
            if pistaComprada :

                print("Ya has comprado la pista. ")
                continue

            else:


                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n¿Qué quieres gastar para obtener la pista de la base alienígena?")
                print("Solo hay una pista por partida. ")
                print(f"Energia: {energia}")
                print(f"Movimientos: {movimientos}/{movFinal}")
                print("1. 250 puntos de energía")
                print("2. 15 movimientos")
                print("3. Cancelar")

                pista = input("Inserta tu opción: ")

                if pista == "1":
                    if energia >=250:
                        energia -= 250

                        if random.randint(0,1) == 0:
                            print(f"La base está en X = ({objetivo_x}, y)")
                        else:
                            print(f"La base está en Y = (x, {objetivo_y})")

                        pistaComprada = True

                    else:
                        print("No tienes suficiente energía para comprar esta opción.")

                elif pista == "2":
                    if movFinal - movimientos >= 15:
                        movFinal -= 15
                        if random.randint(0,1) == 0:
                            print(f"La base está en X = ({objetivo_x}, y)")
                        else:
                            print(f"La base está en Y = (x, {objetivo_y})")
                        pistaComprada = True

                    else:
                        print("No tienes suficientes movimientos para comprar esta opción.")

                elif pista == "3":
                    print("Has cancelado la compra de la pista.")
                    continue

                else:
                    print("Opción no válida.")

        elif decision == "S":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nHas decidido salir de la expedición.")
            print("¡Hasta pronto, astronauta!")
            break

        else:
            print("Opción no válida.")
            continue

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\nPosición anterior: ({x_anterior}, {y_anterior})")
        print(f"Posición actual: ({xJ}, {yJ})")
        print(f"Energía anterior: {energia_anterior}")
        print(f"Energía actual: {energia}")
        print(f"Movimientos realizados: {movimientos}/{movFinal}")
        print(f"Objetos encontrados: {objetosEncontrados}")

        PrimeraRonda = False
        ronda += 1
        


    print("\n ==================================================")
    print("        ~ ~ ~ FIN DE LA EXPEDICIÓN ~ ~ ~           ")
    print("===================================================")
    
    if xJ == objetivo_x and yJ == objetivo_y:
        print("¡MISIÓN COMPLETADA!")
        causaFinal = "Encontró la base alienígena"
    
    if decision == "S":
        print("Has anulado la expedición antes de completarla.")
        causaFinal = "El jugador abandonó la expedición"
        ResultadoF = "Expedición cancelada"

    if energia <= 0:
        print("Te has quedado sin energía.")
        causaFinal = "Se quedó sin energía"
        ResultadoF = "Fracaso"

    elif movimientos >= movFinal:
        print("Te has quedado sin movimientos.")
        causaFinal = "Se quedó sin movimientos"
        ResultadoF = "Fracaso"

    print("\nInforme final:")
    print("Ronda: ", ronda)
    print("Expedición:", nombreE)
    print("Planeta:", nombreP)
    print("Jugador:", nombreJ)
    print(f"Posición inicial: ({xInicial}, {yInicial})")
    print(f"Posición final: ({xJ}, {yJ})")
    print("Energía inicial: ", energiaInicial)
    print("Energía final:", energia)
    print("Movimientos iniciales:", movimientosIniciales)
    print("Movimientos realizados:", movimientos)
    print("Movimientos restantes:", movFinal - movimientos)
    print("Límite de exploración: ±", LIMITE)

    print("Objetos alienígenas encontrados:", objetosEncontrados)
    if Objeto1 :
        print("Objeto alienígena 1 encontrado. ")
    if Objeto2:
        print("Objeto alienígena 2 encontrado. ")
    if Objeto3:
        print("Objeto alienígena 3 encontrado. ")
    if Objeto4:
        print("Objeto alienígena 4 encontrado. ")
    if Objeto5:
        print("Objeto alienígena 5 encontrado. ")
    if objetosEncontrados == 5:
        print("¡Has encontrado todos los objetos alienígenas!")
        ResultadoF = "Victoria, encontró todos los objetos extraterrestres."
    if objetosEncontrados == 0:
        print("No has encontrado ningún objeto alienígena. ")

    if pistaComprada:
        print("Has comprado la pista. ")
    else:
        print("No has comprado la pista. ")

    if Teletransportado:
        print("Los alienígenas te han teletransportado. ")
    if MisilEnergia:
        print("Te han disparado con el misil de energia. ")

    if xJ == objetivo_x and yJ == objetivo_y:
        ResultadoF = "Victoria, encontró la base alienígena"
        if objetosEncontrados == 5:
            ResultadoF = "Victoria total, encontró la base alienígena y todos los objetos extraterrestres"

    print(f"Base encontrada: {'Sí' if xJ == objetivo_x and yJ == objetivo_y else 'No'}")
    print("Base alienígena:", objetivo_x, objetivo_y)
    print("Causa de finalización:", causaFinal)
    print(f"Resultado final: {ResultadoF}")
    print("\n")



def main():

    while True:

        print("\n ==================================================")
        print("          ~ ~ ~ MENÚ PRINCIPAL ~ ~ ~               ")
        print("===================================================")

        print("\n1. Empezar partida")
        print("2. Instrucciones")
        print("3. Salir")

        choice = input("Inserta tu opción: ")

        if choice == "1":
                
            while True:

                jugar()

                while True:

                    respuesta = input("\n¿Volver a jugar? (S/N): ").upper()

                    if respuesta in ("S", "N"):
                        break
                    
                    else:
                        print("Respuesta no válida.")
                    

                if respuesta == "S":
                    continue
                
                elif respuesta == "N":
                    break


            while True:

                salir = input("¿Deseas salir del juego? (S/N): ").upper()

                if salir == "S":
                    print("¡Hasta pronto, astronauta!")
                    exit()

                elif salir == "N":
                    break
                
                else:
                    print("Respuesta no válida.") 
                           




        elif choice == "2":

            print("\n ==================================================")
            print("           ~ ~ ~ INSTRUCCIONES ~ ~ ~               ")
            print("===================================================")
            print("En este juego tu misión es explorar un planeta y encontrar objetos alienígenas, ")
            print("mientras gestionas tu energía y movimientos.")
            print("Cada movimiento consume energía, pero puedes comprar más movimientos con esa misma energía.")
            print("Cada ronda puedes decidir si te quieres mover, comprar movimientos o comprar una pista ")
            print("¡Además, durante la expedición pueden ocurrir eventos aleatorios que te ayudarán o te pondrán las cosas más difíciles!")
            print("¡Disfruta de tu exploración!")
            print("\nPulsa ENTER para volver al menú.")
            input()

        elif choice == "3":

            print("¡Hasta pronto, astronauta!")
            exit()

        else:
            print("Opción no válida.")



main()