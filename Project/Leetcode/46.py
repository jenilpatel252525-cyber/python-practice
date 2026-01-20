a=[0, 0, 0, 3, 12]  

i=0
j=1

while i<len(a) and j<len(a):
    if a[i]==0:
        if a[j]==0:
            j+=1
        else:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            i+=1
            j+=1
    else:
        i+=1
        j+=1

print(a)