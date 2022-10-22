import sys

stack=[]
maxval = 3
for i in range(0,int(maxval)):
    stack.append("")

stackptr=0
choice=-1

#Add
def push(stack,stackptr):
    val= int(input("Enter a value: "))
    if stackptr>maxval:
        print("Stack is full")
    else:
        stack[stackptr] = val
        stackptr= stackptr+1
    return stackptr

#Delete
def pop(stack,stackptr):
    if stackptr < 0:
        print("Stack is empty")
    else:
        stackptr=stackptr-1
        print(stack[stackptr])
    return stackptr

while choice != 3:
    print("Press 1 To PUSH to STACK. Press 2 To POP from STACK. Press 3 To exit this module.")
    choice=int(input())
    if choice ==1:
        stackptr = push(stack,stackptr)
    elif choice==2:
        stackptr= pop(stack,stackptr)
    elif choice==3:
        sys.exit
    else:
        print("Wrong number has been input, Please try again")

print(stack)

