def RecursiveBS(UB, LB, Val):
    mid = int((UB + LB) / 2)
    if LB > UB:
        return -1
    else:
        if Val == SearchArray[mid]:
            return mid
        elif SearchArray[mid] < Val:
            return RecursiveBS(UB, mid + 1, Val)
        elif SearchArray[mid] > Val:
            return RecursiveBS(mid - 1, LB, Val)

SearchArray = ["a", "b", "c", "d"]
LB = 0
UB = 3
Val = input("Enter a value to search: ")
answer = RecursiveBS(3, 0, Val)
if answer == -1:
    print(Val, "not found in array")
else:
    print(Val, "Found at location: ", answer)
