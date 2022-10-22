#Adding to Queue
def AddToQueue(queue,val):
    tempptr = lastindex+ 1
    if tempptr > lastindex:
        tempptr = firstindex
    if  tempptr==startptr:
        return -1
    else:
        endptr=tempptr
        queue[tempptr]= val
        tempptr=tempptr+1
        return 1
queue=[0,0,3,4]
firstindex = 0
lastindex = (len(queue)-1)
startptr= 1
choice=0

while choice!=3:
    choice=int(input("1. To add value in Queue"))
    if choice ==1:
        val=int(input("Enter a value: "))
        ans = AddToQueue(queue,val)
        if ans == 1:
            print(queue)
        else:
            print("Queue is full")




#Delete from Queue
#def delete(val):
 #   if stackptr < 0:
  #      print("Stack is empty")
   # else:
    #    stackptr= stackptr-1
     #   if name[stackptr] = val:

