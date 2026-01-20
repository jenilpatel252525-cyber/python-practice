a=[12, 35, 1, 10, 34, 1] 

if a[0]>a[1]:
    max1=a[0]
    max2=a[1]

else:
    max2=a[0]
    max1=a[1]

for i in range(2,len(a)):
    if a[i]>max1:
        max2=max1
        max1=a[i]
    elif a[i]>max2 and a[i] != max1:
        max2=a[i]
    else:
        continue

print(max2)