def RecursiveBS(Array, UB, LB, Val):
    mid = int((UB + LB) / 2)
    if LB > UB:
        return -1
    else:
        if Val == Array[mid]:
            return mid
        elif Array[mid] < Val:
            return RecursiveBS(Array, UB, mid + 1, Val)
        elif Array[mid] > Val:
            return RecursiveBS(Array, mid - 1, LB, Val)

Array = ["a", "b", "c", "d"]
LB = 0
UB = 3
Val = input("Enter a value to search: ")
ans = RecursiveBS(Array, 3, 0, Val)
if ans == -1:
    print(Val, "not found in array")
else:
    print(Val, "Found at location: ", ans)
