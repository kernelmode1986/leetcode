

import numpy as np
def mergeTwoLists(l1,l2):
    res=[]
    n1=len(l1)
    n2=len(l2)
    i=0
    j=0
    while i<n1 and j<n2:
        if l1[i]<l2[j]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    while i<n1:
        res.append(l1[i])
        i+=1
    while j<n2:
        res.append(l2[j])
        j+=1
    return res
    

def mergeKLists(lists):
    nl=len(lists)
    res=[]
    if nl==0:
        res=[]
    elif nl==1:
        res=lists[0]
    elif nl==2:
        res=mergeTwoLists(lists[0],lists[1])
    else:
        mid=(int)(nl/2)
        t1=mergeKLists(lists[:mid])
        t2=mergeKLists(lists[mid:])
        print(t1,'vs',t2)
        res=mergeTwoLists(t1,t2)
        print('res:',res)
    return res
        
lists=[[1,3],[2,4],[3,5]]
mergeKLists(lists)
