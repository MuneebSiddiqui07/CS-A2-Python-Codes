"""
string1= "Muneeb"
string2= "Siddiqui"
print(string1 + " " + string2)
"""
"""
for x in range(10):
    name = input("Enter your name: ")
    print("Good morning " + name)
"""
"""
PosNum=0
NegNum=0
for x in range(5):
    num = float(input("Enter a number: "))
    if num>0:
        PosNum += 1
    else:
        NegNum += 1
print("Positive Numbers: ", PosNum)
print("Negative Numbers: ", NegNum)
"""

"""
names = ["muneeb", "zaeem", "Hamza", "Sajjad"]
for i in range(len(names)):
    if names[i] == "Hamza":
        print(i)
"""

"""
names=["Muneeb", "Taha", "Rashid", "Sajjad"]
name= input("Enter a name: ")
found = False
for x in range(len(names)):
    if name == names[x]:
        found = True
if found == True:
    print("It is already there")
else:
    names.append(name)
print(names)
"""
"""
Names= ["Empty", "Empty", "Empty", "Muneeb", "Taha"]
count = 0
for x in range(len(Names)):
    if Names[x] == "Empty":
        count += 1
print(count)
"""
"""
Numbers= [10,56,45,34,9,4,13,78,2]
sum=0
for x in range(len(Numbers)):
    if Numbers[x] > 10:
        sum = sum + Numbers[x]
print(sum)
"""
"""
Numbers=[10,32,24,56,75,86]
New= []
for i in range(5,-1,-1):
    New.append(Numbers[i])
print(Numbers)
print(New)
"""
"""
sum= 0
count= 0
num =1
while num != 0:
    num = int(input("Enter number to take average: "))
    sum = sum + num
    count = count + 1
avg=sum/count
print(avg)
"""
"""
def average(sum,count):
    avg = sum/count
    print("Average is: ", avg)
sum1 = float(input("Enter sum: "))
count1 = int(input("Enter count: "))
average(sum1, count1)
"""
"""
def sum(num1, num2, num3):
    total = num1 + num2 + num3
    print(total * 2)
sum1 = float(input("Enter first number: "))
sum(2, 3,4)
"""
"""
def table(val):
    for i in range(11):
        ans = val*i
        print(str(val) + " x " + str(i) + " = " + str(ans))

num = int(input("Enter integer whose table you want to see: "))
table(num)
"""
"""
def LargestTable(val):
    largest = 0
    for i in range(len(val)):
        if val[i] > largest:
            largest = val[i]
    for x in range(11):
        ans = largest * x
        print(str(largest) + " x " + str(x) + " = " + str(ans))
Numbers = [45,34,23,87,96,23]
LargestTable(Numbers)
"""
"""
def div(num1,num2):
    ans = num1//num2
    return ans
val1 = int(input("Enter a dividend: "))
val2= int(input("Enter a divisor: "))
x=div(val1,val2)
print(x)
"""
"""
def mod(num1,num2):
    ans= num1%num2
    return ans
val1= float(input("Enter a dividend: "))
val2 = float(input("Enter a divisor: "))
ans = mod(val1,val2)
print(ans)
"""
"""
Name= input("Enter a name: ")
for x in range(0,len(Name)):
    if Name[x] == " ":
        first = Name[0:x]
        last = Name[x + 1: len(Name)]
print("First name: " + first)
print("Last name: " + last)

"""
"""
#Declare arrayData:Array[0:9]
arrayData= [10, 5, 6,7,1,12,13,15,21,8]
def Linearsearch(number):
    for i in range(0, len(arrayData)):
        if arrayData[i] == number:
            return True
    return False
val= int(input("Enter a number to search: "))
found = Linearsearch(val)
if found == True:
    print("It was found")
else:
    print("It was not found")
arrayData=[1,2,5,6,7,8,10,12,13,15,21]

def BinarySearch(num):
    UB= len(arrayData)
    LB= 0
    found = False
    while found == False and LB > UB:
        mid = int((LB + UB)) // 2
        if num == arrayData[mid]:
            found = True
            return True
        elif num < arrayData[mid]:
            UB = mid - 1
        elif num > arrayData[mid]:
            LB = mid + 1
val = int(input("Entere a value to search: "))
found = BinarySearch(val)
if found == True:
    print("Value found")
else:
    print("Value not found")
"""
#Insertion Sort
cardata=[4,3,24,54,1,3,5,6,7,3,4]
def insertionsort():
    for pointer in range(1,len(cardata)):
        holeposition = pointer
        valuetoinsert = cardata[pointer]
        while valuetoinsert < cardata[holeposition-1] and holeposition>0:
            cardata[holeposition] = cardata[holeposition-1]
            holeposition= holeposition-1
        cardata[holeposition] = valuetoinsert
    print(cardata)
insertionsort()

    