a=[2, 3, 1, 1, 4]

i=0

jump=0

while i<len(a):
    j=a[i]
    l=0
    p=0
    for k in range(i+1,i+j+1):
        if k<len(a):
            if a[k]==0:
                continue
            if k+a[k]>=l:
                l=k+a[k]
                p=k
    i=p
    jump+=1
    
print(jump)