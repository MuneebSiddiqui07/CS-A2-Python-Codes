#push

for i in range(0,int(arraysize)):
    stack.append("")

def push(stack,val):
    if stackptr>arraysize:
        return -1
    else:
        stack[stackptr] = val
        stackptr= stackptr+1
    return stackptr

stack=[]
stackptr = 0
arraysize = len(stack)
val = int(input("Enter a value: "))
ans = push(stack,val)
if ans==-1:
    print("Stack is Full")
else:
    print()
