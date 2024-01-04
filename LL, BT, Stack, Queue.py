# Binary Tree Addition
TreeArray = [[0]*3 for i in range(20)]
freeptr = 0
startptr = -1

def AddNode():
    global freeptr, startptr
    if freeptr > 19:
        print("Tree is full")
    else:
        val = int(input("Enter the value to add: "))
        TreeArray[freeptr][0] = -1
        TreeArray[freeptr][1] = val
        TreeArray[freeptr][2] = -1
        if startptr == -1:
            startptr = 0
        else:
            currentptr = startptr
            added = False
            while added == False:
                if val < TreeArray[currentptr][1]:
                    if TreeArray[currentptr][0] == -1:
                        TreeArray[currentptr][0] = freeptr
                        added = True
                    else:
                        if TreeArray[currentptr][2] == -1:
                            TreeArray[currentptr][2] = freeptr
                            added = True
        freeptr = freeptr + 1
# Binary Tree Searching
def SearchTree():
    global freeptr, startptr
    currentptr = startptr
    val = int(input("Enter the value to search: "))
    found = False
    while found == False:
        if TreeArray[currentptr][1] == val:
            found = True
        elif TreeArray[currentptr][1] > val:
            currentptr = TreeArray[currentptr][0]
        else:
            currentptr = TreeArray[currentptr][2]

# Linked List Addition
class LLNode():
    def __init__(self, data, ptr):
        self.data = 0
        self.ptr = -1
List = [LLNode(0,-1) for x in range(10)]
print(List)
freeptrLL = 5
startptrLL = 0
def AddLL():
    global freeptrLL  , startptrLL, List
    if freeptrLL > 9 or freeptrLL < 0:
       print("List is full")
    else:
        val = int(input("Enter the value to add: "))
        emptylist = freeptrLL
        freeptrLL = List[freeptrLL].ptr

        NewNode = LLNode(val, -1)
        List[emptylist] = NewNode

        currentptr = startptrLL
        #previousptr = -1
        while currentptr != -1 and List[currentptr].data < val:
            previousptr = currentptr
            currentptr = List[currentptr].ptr

        if currentptr == startptrLL:
            List[emptylist].ptr = startptrLL
            startptrLL = emptylist
        else:
            List[emptylist].ptr = List[previousptr].ptr
            List[previousptr].ptr = emptylist

def outputNode():
    global startptr, List
    currentptr = startptr
    while currentptr != -1:
        print(List[currentptr].data)
        currentptr = List[currentptr].ptr
# Linked List Deletion
# Linked List Searching
def searchLL():
    global startptrLL, List
    val = int(input("Enter the Value to search"))
    currentptr = startptrLL
    while currentptr != -1:
        if val == List[currentptr].data:
            return True
        else:
            currentptr = List[currentptr].ptr
    return False

# Stack Addition
stackptr = 0
stack = [0]* 10
def push():
    global stackptr
    if stackptr > 9:
        print("stack is full")
    else:
        val = int(input("enter the value to add: "))
        stack[stackptr] = val
        stackptr = stackptr + 1

# Stack Deletion
def pop():
    global stackptr
    if stackptr == 0:
        print("Stack is empty")
    else:
        stackptr = stackptr - 1
        val = stack[stackptr]
        print(val)

# Linear Queue Addition

# Linear Queue Deletion
# Circular Queue Addition
# Circular Queue Deletion
# Binary Searching
# Recursive Binary Searching
# Insertion Sort
data = [6,1,5,2,7,9,74,23,11,5]
def insertionsort():
    global data
    for pointer in range(1,len(data)):
        valuetoinsert = data[pointer]
        holeposition = pointer
        while holeposition> 0 and valuetoinsert < data[holeposition-1]:
            data[holeposition]= data[holeposition-1]
            holeposition = holeposition -1
        data[holeposition] = valuetoinsert
    print(data)

# 2D Insertion Sort
# Bubble Sort (Efficient)
# Bubble Sort (InEfficient)

