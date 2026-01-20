a=[1, 2, 1, 0, 1, 1, 1]
k=2
sum=0
l=0
legth=0
i=0
j=0

while i<len(a) and j<len(a):
    sum=sum+a[i]
    while sum>k:
        sum=sum-a[j]
        j=j+1
    legth=max(i-j+1,legth)
    i+=1

print(legth)

    