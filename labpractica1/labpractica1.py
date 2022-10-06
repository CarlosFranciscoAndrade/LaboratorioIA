# Practica del Laboratorio
# Inteligencia Artificial

import random

# Funciones del programa:
# funcion de la captura de los datos para el laberinto por teclado
def datos():
    try:
        numero_filas = int(input('Introdusca el numero de filas: '))
        numero_columnas = int(input('Introdusca el numero de columnas: '))
    except:
        print("los datos solo pueden ser numeros enteros")
        return datos()
    if numero_filas<4 and numero_columnas<4:
        print("los valores minimos para paredes y columnas deben ser 5 o mas")
        return datos()
    estructura = int(input('Desea establecer el numero de paredes o espacios libres? \n 1:paredes \n 2:espacios\n'))    
    if estructura!=1 and estructura!=2:
        eleccion = int(input('No existe esa opcion.\nPor favor elija de nuevo.\nDesea establecer el numero de paredes o espacios libres? \n 1:paredes \n 2:espacios\n'))

    if estructura==1:
        eleccion = int(input('Introdusca el numero de paredes: '))
    if estructura==2:    
        eleccion = int(input('Introdusca el numero de espacios: '))
    return [numero_filas,numero_columnas,estructura,eleccion]

# funcion que crea el laberinto
def crearlaberinto(numero_filas , numero_columnas,estructura):
    mapa_laberinto=[]
    for filas in range(0,numero_filas):
        fila_laberinto=[]
        for columnas in range(0,numero_columnas):
            if(estructura==1):
                if(filas==0 or columnas==0 or filas==numero_filas-1 or columnas==numero_columnas-1):
                    fila_laberinto.append('#')
                else:
                    fila_laberinto.append(' ')
            if(estructura==2):
                if(filas==0 or columnas==0 or filas==numero_filas-1 or columnas==numero_columnas-1):
                    fila_laberinto.append(' ')
                else:
                    fila_laberinto.append('#')
        mapa_laberinto.append(fila_laberinto)
    return  mapa_laberinto

# funcion que muestra el laberinto
def mostrarlaberinto(laberinto):
    for row in laberinto:
        print(" ".join(row))

# funcion que agrega las paredes
def paredes(laberinto,estructura,eleccion):
    if(eleccion==0):
        return
    if(estructura==1):
        x,y=[random.randint(1,len(laberinto)-2),random.randint(1,len(laberinto[0])-2)]
        if(laberinto[x][y]==" "):
            if(laberinto[x][y-1]==" " or
            laberinto[x][y+1]==" " or
            laberinto[x+1][y]==" " or
            laberinto[x-1][y]==" " ):
                laberinto[x][y]="#"
                eleccion=eleccion-1
        return paredes(laberinto,estructura,eleccion)
    if(estructura==2):
        x,y=[random.randint(1,len(laberinto)-2),random.randint(1,len(laberinto[0])-2)]
        if(laberinto[x][y]=="#"):
            if(laberinto[x][y-1]=="#" or
            laberinto[x][y+1]=="#" or
            laberinto[x+1][y]=="#" or
            laberinto[x-1][y]=="#" ):
                laberinto[x][y]=" "
                eleccion=eleccion-1
        return paredes(laberinto,estructura,eleccion)
# funcion que genera al agente
def inicioagente( laberinto = None, jugador = None):
    x, y = [random.randint( 1, len( laberinto ) - 2 ), random.randint( 1, len( laberinto[ 0 ] ) - 2)]
    if( laberinto[x][y] == " " ):
        laberinto[x][y] = jugador
        return [x,y]
    else:
        return inicioagente(laberinto, jugador)
# funcion que crea los objetivos(Pelotas)
def objetivo( laberinto, jugador, meta ):
    x, y = [ random.randint( 1, len( laberinto ) - 2 ), random.randint( 1, len( laberinto[ 0 ] ) - 2)]
    if( laberinto[x][y] != "#" and laberinto[x][y] != jugador):
        laberinto[x][y] = meta
        return [x,y]    
    else:
        return objetivo( laberinto, jugador, meta )
numero_filas,numero_columnas,estructura,eleccion=datos()
laberinto=crearlaberinto(numero_filas,numero_columnas,estructura)
paredes(laberinto,estructura,eleccion)
inicioagente(laberinto,"*")
objetivo(laberinto,"*","O")
mostrarlaberinto(laberinto)


