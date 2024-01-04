"""
friends= ["Sajju", "Aziz", "Rafay"]
num=[1,2,3,4,5]
friends.extend(num)
friends.pop()
friends.append("Amail")
friends.insert(1, "Usaim")
friends.sort()      #sort in alphabetical order
friends.reverse()   #reverses the order of the items in the list
friends2= friends.copy()      #list friends2 copies friends

print(friends.index("Aziz"))
print(friends2)

RegionList=[
    ["Canada", "UK"],
    ["India","Pakistan"],
    ["Germany", "US"]
]

print(RegionList)

sand = '.'
Grid= [
    [sand for col in range(30)]
    for row in range(10)]
]
print(Grid)


grocery=[["eggs", "bread"], ["milk", "meat"], [50]]
print(grocery[0][1])

for inner_list in grocery:
    for grade in inner_list:
        print(grade, end=" ")


flag = True
sum = 0
count = 0
while flag == True:
    num = float(input("Enter Numbers to take average. Type 0 to end: "))
    if num == 0:
        flag = False
    else:
        count = count+ 1
        sum = sum + num
avg = sum/count
print(avg)
"""


array = [[0] * 3 for i in range(9)]
for x in range(9):
    print(array[x])
