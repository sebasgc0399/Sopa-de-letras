def knapsack(capacidad, items, cantItems):
    K = [[0 for x in range(capacidad + 1)] for x in range(cantItems + 1)]

    # Construir la tabla K[][] de abajo hacia arriba
    for i in range(cantItems + 1):
        for j in range(capacidad + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif items[i-1][1][0] <= j:
                K[i][j] = max(items[i-1][1][1] + K[i-1][j-items[i-1][1][0]],  K[i-1][j])
            else:
                K[i][j] = K[i-1][j]

    # Almacenar el resultado del valor total y construir la lista de itemsMochila
    res = K[cantItems][capacidad]
    itemsMochila = []
    itemsRestantes = []
    valorTotal = 0
    valorTotalRestante = 0

    for i in range(cantItems, 0, -1):
        
        if res <= 0:
            break
        if res == K[i - 1][capacidad]:
            itemsRestantes.append(items[i - 1][0])
            valorTotalRestante = valorTotalRestante + items[i - 1][1][1]
            continue
        else:
            # Este item está incluido.
            itemsMochila.append(items[i - 1][0])
            valorTotal = valorTotal + items[i - 1][1][1]
            # Ya que este peso está incluido su valor es restado
            res = res - items[i - 1][1][1]
            capacidad = capacidad - items[i - 1][1][0]

    return itemsMochila, valorTotal, itemsRestantes, valorTotalRestante

capacidad = int(input("Ingrese la capacidad maxima de la mochila: "))
cantItems = int(input("Ingrese la cantidad de items: "))
items = []

for i in range(cantItems):
    nombre = input("Descripcion del item: ")
    peso = int(input("Ingrese el peso del item: "))
    valor = int(input("Ingrese el valor del item: "))
    item = [nombre, [peso, valor]]
    items.append(item)

itemsMochila, valorTotal, itemsRestantes, valorTotalRestante = knapsack(capacidad, items, cantItems)
print("La combinacion optima es ", itemsMochila, " con un valor total de ", valorTotal)
print("La combinacion de elementos que no se llevan es ", itemsRestantes," con un valor total de ", valorTotalRestante)