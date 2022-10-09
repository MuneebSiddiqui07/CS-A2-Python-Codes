cardata=[8,4,3,6,5,7,9,8,1,3,2]
for pointer in range(1,11) :
    valuetoinsert= cardata[pointer]
    holeposition = pointer
    while holeposition > 0 and cardata[holeposition-1] > valuetoinsert:
        cardata[holeposition] = cardata[holeposition-1]
        holeposition = holeposition - 1
        cardata[holeposition] = valuetoinsert
print (cardata)
