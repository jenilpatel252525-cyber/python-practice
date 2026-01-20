a=[[1,2],[3,4],[5,6],[7,8]]
r=2
c=3

m=len(a)
n=len(a[0])

b=sum(a,[])

i=0
j=0
d=[]
e=[]

while i<len(b):
    if r*c==m*n:
        d.append(b[i])
        i+=1
        j+=1
        if j>=c:
            e.append(d)
            d=[]
            j=0
    else:
        e=a
        break

print(e)

