alpha = ['a','b','c','d','e','f','g','h','i','j']

def BinaryS(value):
    LB = 0
    UB = 9
    isfound = False
    while UB>=LB and isfound == False:
        mid = (UB+LB)//2
        if value == alpha[mid]:
           isfound = True
        elif value > alpha[mid]:
            LB = mid +1
        elif value < alpha[mid]:
            UB = mid - 1
    if isfound == True: 
        return mid 
    else:
        return -1
    
x = input ("Enter an alphabet: ")
answer = BinaryS(x)
if x != -1:
    print ("The alphabet", x, "is found at", answer)
else:
    print ("The alphabet", x, "is not present in the array")
