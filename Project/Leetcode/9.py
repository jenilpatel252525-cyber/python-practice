a=[7,6,5,2]

i=0
j=1
k=0
max1=0
max2=0
max=0

while i < len(a):
    while j < len(a):
        k=a[j]-a[i]
        if k>max:
            max1=i+1
            max2=j+1
            max=k
        j+=1
    i+=1
    j=i+1


print(max1,max2)