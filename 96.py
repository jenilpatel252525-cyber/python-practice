a=[1,2,2]
b=[[]]
curr=[]

def subsets(i):
    for j in range(i,len(a)):
        curr.append(a[j])
        if curr not in b:
            b.append(curr[:])
        subsets(j+1)
        curr.pop()
            
subsets(0)

print(b)