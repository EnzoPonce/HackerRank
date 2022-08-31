arr = [5,5,5,5,5]

def miniMaxSum(arr):
    suma = 0
    suma2 = 0
    maximo = max(arr)
    minimo = min(arr)
    for element in arr:
        suma = sum(arr)
        suma2 = sum(arr)
    suma = suma-maximo
    suma2 = suma2 - minimo 
    print(suma, suma2)    

miniMaxSum(arr)

