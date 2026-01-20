a=[1,2,2]

b=[[]]

curr=[]

def subset(i):
    print(i,0)
    if i>=len(a):
        print(i,1)
        return
    for j in range(i,len(a)):
        print(j,2)
        print(curr,3)
        curr.append(a[j])
        if curr not in b:
            b.append(curr[:])
        print(curr,4)
        subset(j+1)
        print(curr,5)
        curr.pop()
        print(curr,6)
        print(j,7)
        
subset(0)
        
print(b)