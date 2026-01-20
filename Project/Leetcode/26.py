a=[1,3,4,7,9,10]
t=2
i=0
p=0

while i<len(a):
    if i==len(a)-1:
        p+=t
        i+=1
    elif a[i+1]-a[i]>=t:
        p+=t
        i+=1
    else:
        p+=a[i+1]-a[i]
        i+=1

print(p)

