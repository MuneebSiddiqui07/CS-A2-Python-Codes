cardata = [8,4,3,6,5,7,9,8,1,3,2]
for pointer in range(1,11) :
    valuetoinsert= cardata[pointer]
    holeposition = pointer
    while holeposition > 0 and cardata[holeposition-1] > valuetoinsert:
        cardata[holeposition] = cardata[holeposition-1]
        holeposition = holeposition - 1
    cardata[holeposition] = valuetoinsert
print(cardata)


cardata = [8, 4, 3, 6, 5, 7, 9, 8, 1, 3, 2]
def insertionsort(array):
    for pointer in range(1, len(cardata)):
        valuetoinsert = cardata[pointer]
        holeposition = pointer
        while holeposition > 0 and valuetoinsert < cardata[holeposition-1]:
            cardata[holeposition] = cardata[holeposition-1]
            holeposition = holeposition - 1
        cardata[holeposition] = valuetoinsert


insertionsort(cardata)
print(cardata)

def insertionsort(array):
    for pointer in range(1,11):
        valuetoinsert = array[pointer]
        holeposition = pointer
        while array[holeposition-1] > valuetoinsert and holeposition > 0:
            array[holeposition] = array[holeposition-1]
            holeposition = holeposition-1
        array[holeposition] = valuetoinsert

cardData = [1,4,1,52,2,34,5,6,23]
def insertionsort1(array):
    for Pointer in range(1,len(array)):
        holeposition = Pointer
        valuetoinsert = array[Pointer]
        while holeposition > 0 and valuetoinsert < array[holeposition-1]:
            array[holeposition] = array[holeposition-1]
            holeposition = holeposition -1
        array[holeposition] = valuetoinsert





















