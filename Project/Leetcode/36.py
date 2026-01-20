a=[0,1,0,0,1,0,0,0,1]

i=0

while i<len(a):
    if i==0:
        if a[i+1]==0:
            a[i]=1
    elif i==len(a)-1:
        if a[i-1]==0:
            a[i]=1
    else:
        if a[i+1]==0 and a[i-1]==0:
            a[i]=1
    i+=1

print(a)