a=[1,2,3,2,4,5,2,2,3,4,5,6]

b={}
d={}
e={}

max=0
c=None

for i in range(len(a)):
    if a[i] in b:
        b[a[i]]=b[a[i]]+1
        e[a[i]]=i
    else:
        b[a[i]]=1
        d[a[i]]=i
    if b[a[i]]>max:
        max=b[a[i]]
        c=a[i]

print(e[c]-d[c])

