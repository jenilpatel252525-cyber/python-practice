a=[1,2,3,5,6,8,10,11]
c=[]
b=[]
i=0

for i in range(0,len(a)):
    if i<len(a)-1:
        if a[i+1]==a[i]+1:
            if i==len(a)-2:
                b.append(f"{a[i]}-{a[i+1]}")
            else:
                c.append(a[i])
        else:
            if i==len(a)-2:
                b.append(f"{a[i]}")
                b.append(f"{a[i+1]}")
            c.append(a[i])
            if len(c)>1:
                b.append(f"{c[0]}-{c[len(c)-1]}")
            else:
                b.append(f"{c[0]}")
            c=[]
    else:
        break
        
print(b)