a=[0, 1, 0, 3, 12]  

i=0
j=len(a)-1

while i<j:
    if a[i]==0:
        if a[j]==0:
            j=j-1
        else:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            j=j-1
            i=i+1
    else:
        i=i+1

print(a)