#Declare record type
class tree:
    def _init_(self): #yahan pr self ka kia kaam hy
        self.lp= 0
        self.rp =0
        self.data = ""

# Make a 2d array of type Tree
BT=[tree() for i in range (10)]

# initialize the Binary tree
def intialize():
    global fp,rp # is declare ki kia zarorat thi direct value assign kardetay line 19 mn toh kia isuue hota?
    for count in range (10):
        BT[i].rp= -1
        BT[i].lp = -1
        BT[i].data = ""
    rp = 0
    fp = 0

def insertnode(val):
    global fp # yahan pr dobara declare kyu kia?
    cn= rp
    isadded = False
    if  BT[cn].data == "":
        BT[cn].data = val
        fp = fp +1
    elif fp > 10:
        print ("Overflow has occured")
    else:
        BT[fp].data = val
        while isadded == False:
            if val>BT[cn].data:
                if BT[cn].rp == -1:
                    BT[cn].rp= fp
                    isadded = True
                else:
                    cn = BT[cn].rp
            else:
                val<BT[cn].data:
                if BT[cn].lp == -1:
                    BT[cn].lp=fp
                    isadded = True
                else:
                    cn = BT[cn].rp
        fp=fp+1













