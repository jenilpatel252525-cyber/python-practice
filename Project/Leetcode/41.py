a=[1,7,3,4,5,6]

left=0
right=0
sum=0

b={}

for i in range(len(a)):
    b[i]=sum
    sum=sum+a[i]

for i in b:
    if b[i]==(sum-a[i])/2:
        print(i)

print(b)


