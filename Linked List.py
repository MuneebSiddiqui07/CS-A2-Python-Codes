    # Declare record type to store data and pointer
class ListNode:
    def __init__(self):
        self.data = ""
        self.ptr = -1


List = [ListNode() for i in range(9)]       # declaring array with datatype created above 'ListNode'
startptr = 0
freeptr = 0

def InitializeList():
    global startptr, freeptr
    for i in range(9):
        List[i].data = ""
        List[i].ptr = i+1
    List[8].ptr = -1

def InsertNode(val):
    global startptr, freeptr
    if freeptr < 0 or freeptr > len(List):                  # if condition is true it means list is full
        return -1
    else:
        # storing
        newNodePtr = freeptr                # freeptr ki value lost na ho isliay newnodeptr ko use kia
        List[newNodePtr].data = val         # storing val in the free space
        freeptr = List[freeptr].ptr         # incrementing freeptr

        # searching for correct position
        previousNodeptr = -1
        currentNodePtr = startptr            # so that we can compare from the start
        # first condition checks if end of list is reached
        # second condition checks after which node val is greater (ascending order)
        while currentNodePtr != -1 and List[currentNodePtr].data < val:
            previousNodeptr = currentNodePtr
            currentNodePtr = List[currentNodePtr].ptr

        # changing pointers for correct placement of node
        if previousNodeptr == startptr:
            List[newNodePtr].ptr = startptr         # inserting node at start
            startptr = newNodePtr
        else:
            List[newNodePtr].ptr = List[previousNodeptr].ptr  # inserting node in between
            List[previousNodeptr].ptr = currentNodePtr


def deletenode(val2):
    global startptr, freeptr, previousNodePtr
    currentNodePtr = startptr           # start comparision from beginning

    # first condition checks if data is present
    # second condition checks if value is found or not
    while currentNodePtr != -1 and List[currentNodePtr].data != val2:
        previousNodePtr = currentNodePtr
        currentNodePtr = List[currentNodePtr].ptr           # finding index value of parameter

    if currentNodePtr != -1:
        if currentNodePtr == startptr:
            startptr = List[startptr].ptr
        else:
            List[previousNodePtr].ptr = List[currentNodePtr].ptr
    else:
        print("value is not in list")

    List[currentNodePtr].data = 0
    List[currentNodePtr].ptr = freeptr
    freeptr = currentNodePtr


def findelement(val3):
    global startptr, freeptr
    currentNodePtr = startptr
    while currentNodePtr != -1 and List[currentNodePtr].data != val3:
        currentNodePtr = List[currentNodePtr].ptr
    return currentNodePtr

def outputnodes():
    global startptr, freeptr
    currentNodePtr = startptr
    while currentNodePtr != -1:
        print(str(List[currentNodePtr].data))
        currentNodePtr = List[currentNodePtr].ptr

outputnodes()
