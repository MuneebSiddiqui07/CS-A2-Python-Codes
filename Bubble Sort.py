# efficient
data = [29,5,4,7,2,6]
def bubblesort(array):
    boundary = len(data) - 1
    swaps = True
    while swaps == True:
        swaps = False
        for y in range(0, boundary):
            if array[y+1] < array[y]:
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp
                swaps = True
        boundary = boundary - 1

bubblesort(data)
print(data)


# inefficient
data2=[29,5,4,7,2,6]
def bubblesort2(array):
    for i in range(0,len(array)):
        for y in range(0, len(array)-1):
            if array[y] > array[y+1]:
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp
    return array
print(bubblesort2(data2))
















