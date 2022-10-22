def binarysearch(val):
    cn = 0
    isfound = False
    while isfound == False and cn != -1:
        if BT[cn].data = val:
            isfound = True
        elif val>BT[cn].data:
            cn =BT[cn].rp
        elif val<BT[cn].data:
            cn =BT[cn].lp
    if isfound== True:
        return cn
    else:
        return -1
