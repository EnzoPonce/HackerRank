def lonelyinteger(a):
    nueva = []
    valor = 0
    for element in a:
        nueva = (a.count(element) == 1)
        if nueva is True:
            valor += element 
    return valor
    
a = [1,2,3,4,1,2,3,5]

lonelyinteger(a)