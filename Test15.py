import random 
import numpy as np

#Clase que indica la direccion o el cursor de la palabra dentro de la sopa de letra
class Cursor:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.avanX = [-1, 0, 1][random.randint(0,2)]
        self.avanY = [-1, 0, 1][random.randint(0,2)]
        if self.avanX == 0 and self.avanY == 0:
            self.avanX = 1

    def next(self, pasos=1):
        self.fila += pasos * self.avanX
        self.columna += pasos * self.avanY

    def es_valido(self, dimension):
        return 0 <= self.fila < dimension and 0 <= self.columna < dimension

    def __str__(self):
        return f"[{self.fila} {self.avanX}, {self.columna} {self.avanY}]"

#Clase que genera la matrix y la rellena con las palabras enviadas y rellena los espacios vacios aleatoriamente
class Matrix:
    def __init__(self, dimension):
        valores = [' '] * dimension * dimension
        self.dimension = dimension
        self.matriz = np.array(valores).reshape((dimension, dimension))
        self.libres = dimension * dimension
        self.palabras = []

    def __getitem__(self, cursor):
        if cursor.es_valido(self.dimension):
            return self.matriz[cursor.fila][cursor.columna]
        else:
            return ' '

    def __setitem__(self, cursor, value):
        if cursor.es_valido(self.dimension):
            
            if self.matriz[cursor.fila][cursor.columna] == ' ':
                self.libres -= 1
            self.matriz[cursor.fila][cursor.columna] = value

    def fill_empty_spaces(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matriz[i][j] == ' ':
                    self.matriz[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def put(self, palabra):
        intentos = 0
        while intentos < 100:
            x, y = random.randint(0, self.dimension - 1), random.randint(0, self.dimension - 1)
            cursor = Cursor(x, y)

            largo = len(palabra)
            if self.cabe_palabra(cursor, largo):
                restantes = largo
                for indice in range(largo):
                    if self[cursor] == ' ' or self[cursor] == palabra[indice]:
                        self[cursor] = palabra[indice]
                        restantes -= 1
                    cursor.next()

                if restantes == 0:
                    self.palabras.append((x, y, cursor.avanX, cursor.avanY, palabra))
                    return True
            intentos += 1
        return False
    
    def cabe_palabra(self, cursor, largo):
        fila_final = cursor.fila + cursor.avanX * (largo - 1)
        columna_final = cursor.columna + cursor.avanY * (largo - 1)
        return 0 <= fila_final < self.dimension and 0 <= columna_final < self.dimension

    def __str__(self):
        regla = f"   {('0 1 2 3 4 5 6 7 8 9 ' * int (self.dimension / 10 + 1))[:self.dimension * 2]}\n"
        linea = regla
        for i in range(self.dimension):
            linea += f"{i:2d} {' '.join(self.matriz[i].tolist())}\n"
        return linea + regla

#Funcion para Buscar las palabras en la Matriz de palabras
def Buscar(cursor):
    palabra = input("Ingresa palabra a buscar: ")
    Validar = False

    for i in range(len(matriz.palabras)):
        if cursor[i][4] == palabra:
            Validar = True
            fila = cursor[i][0]
            columna = cursor[i][1]
            X = cursor[i][2]
            Y = cursor[i][3]
            if X == 0 and Y == 1: # Horizontal + Hacia la Derecha
                for j in range(len(cursor[i][4])):
                    print(cursor[i][4][j], "- [",fila+j,",",columna,"]")
            elif X == 0 and Y == -1: # Horizontal + Hacia la Izquierda
                for j in range(len(cursor[i][4])):
                    print(cursor[i][4][j], "- [",fila-j,",",columna,"]")
            elif X == 1 and Y == 0: # Vertical + Hacia abajo
                for j in range(len(cursor[i][4])):
                    print(cursor[i][4][j], "- [",fila,",",columna+j,"]")
            elif X == -1 and Y == 0: # Vertical + Hacia arriba
                for j in range(len(cursor[i][4])):
                    print(cursor[i][4][j], "- [",fila,",",columna-j,"]")
            elif X == -1 and Y == -1:  # Diagonal + Izquierda/Arriba
                for j in range(len(cursor[i][4])):
                    print(cursor[i][4][j], "- [",fila-j,",",columna+j,"]")
            elif X == 1 and Y == 1:  # Diagonal + Derecha/Abajo
                for j in range(len(cursor[i][4])):
                    print(cursor[i][4][j], "- [",fila+j,",",columna+j,"]")
            elif X == -1 and Y == 1: # Diagonal + Derecha/Arriba
                for j in range(len(cursor[i][4])):
                    print(cursor[i][4][j], "- [",fila+j,",",columna-j,"]")
            elif X == 1 and Y == -1: # Diagonal + Izquierda/Abajo
                for j in range(len(cursor[i][4])):
                    print(cursor[i][4][j], "- [",fila-j,",",columna+j,"]")
            else:
                print('Error de las coordenadas')

    if Validar == False:
        print('"',palabra,'" Not found')
        Validar = False    
            
    switch = input("Desea seguir buscando (y) o (n):  ")
    if switch == 'y' or switch == 'Y':
        Buscar(cursor)

tamaño = input("Ingrese el tamaño NxN: ")
cantidad = input("Cantidad de palabras: ")
lista_palabras=[]

for i in range(int(cantidad)):
    palabras=input("Ingrese palabra: ")
    lista_palabras.append(palabras)

matriz = Matrix(int(tamaño))

for palabra in lista_palabras:
    intentos = 0
    while not matriz.put(palabra) and intentos < 100:
        intentos += 1

matriz.fill_empty_spaces()  # Llena los espacios vacíos después de colocar todas las palabras

print(matriz)
Buscar(matriz.palabras)
    