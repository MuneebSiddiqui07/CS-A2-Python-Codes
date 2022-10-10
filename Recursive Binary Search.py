def RecursiveBS(SearchArray, UB, LB, Val):
    if LB > UB:
        return -1
    else:
        mid = int((UB + LB) // 2)
        if Val == SearchArray[mid]:
            return mid
        elif SearchArray[mid] < Val:
            return RecursiveBS[SearchArray, UB, mid + 1, Val]
        elif SearchArray[mid] > Val:
            return RecursiveBS[SearchArray, mid - 1, LB, Val]


SearchArray = ["a", "b", "c", "d"]
LB = 0
UB = 3
Val = input("Enter a value to search: ")
Result = RecursiveBS(SearchArray, UB, LB, Val)
if Result == -1:
    print(Val, "not found in array")
else:
    print(Val, "Found at location: ", Result)
