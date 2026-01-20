rows=11

# a=[1]

# b=[1,1]

# c=[1,2,1]

# d=[1,3,3,1]

# e=[1,4,6,4,1]

# f=[1,5,10,10,5,1]

# g=[1,6,15,20,15,6,1]

# h=[1,7,21,35,35,21,7,1]

# i=[1,8,28,56,70,56,28,8,1]

# j=[1,9,36,84,126,126,84,36,9,1]


a=[]
j=0

while j<rows:

    p=[]
    i=0
    n=j+1
    if len(a)>0:
        h=a[len(a)-1]
    
    while i<n:
        if i==0 or i==n-1:
            p.append(1)
            i+=1
        else:
            p.append(h[i]+h[i-1])
            i+=1

    a.append(p)
    j+=1

i=0
row=11
q=[]
while i < row:
    if i==0 or i==row-1:
        q.append(1)
        i+=1
    else:
        q.append(int(q[i-1]*(row-i)/i))
        i+=1

print(q)