a=[5,2,1]
b=[0]
curr=[]

def subsetsum(i):
    for j in range(i,len(a)):
        curr.append(a[j])
        if sum(curr) not in b: 
            b.append(sum(curr))
        subsetsum(j+1)
        curr.pop()
    
subsetsum(0)

print(b)