def diagonalDifference(arr):
    new = 0
    new2 = 0
    for x in range(len(arr)):
        new += arr[x][x]   
    for i in range(len(arr)-1,-1,-1):
        new2 += arr[i][-i-1]
    diferencia = abs(new - new2)
    return diferencia      
            
        
arr = [[1,2,3], [4,5,6], [7,8,15]]
diagonalDifference(arr)