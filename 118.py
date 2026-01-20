a=[1,3,4,6,7,8,10]

target=10

curr=None

i=0
j=len(a)-1

while i<j:
    curr=a[i]+a[j]
    if curr==target:
        break
    elif curr>target:
        j-=1
    else:
        i+=1
        
print(i,j)