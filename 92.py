k=2
n=4
a=[]
curr=[]

def nums(i):
    if len(curr)==k:
        a.append(curr[:])
        return
    for j in range(i,n+1):
        curr.append(j)
        nums(j+1)
        curr.pop()