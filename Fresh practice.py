alpha = ['a','b','c','d','e','f','g','h','i','j']

def BinaryS(value):
    LB = 1
    UB = 10
    isfound=false
    mid= [(UB+LB)/2]
    while UB>=LB or isfound = false :
        if value = alpha [mid]:
           isfound = true
        elif value > alpha [mid]:
               LB = mid +1
        elif value < alpha [mid]:
              UB = mid - 1

    x = input ("Enter an alphabet: ")
    if isfound = true:
        print ("The alphabet", x "is found at", BinaryS(x))
    elif print ("The alphabet", x "is not present in the array")


