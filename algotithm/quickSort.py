def quickSort(array):
    if len( array ) < 2:
        return array
    else:
        pivot = array[1]
        less = [i for i in array[1:] if i <= pivot]
        grater = [i for i in array[1:] if i > pivot]
    return quickSort( less ) + [pivot] + quickSort( grater )

print(quickSort([10,5,2,3,5,8,7,1,2]))