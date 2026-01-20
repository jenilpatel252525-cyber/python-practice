a=[0,1,0,0,2,3,0]
i=0
j=0
# while j<len(a):
#     if a[i]==0:
#         a.remove(a[i])
#         a.append(0)
#         j=j+1
#     else:
#         i=i+1
#         j=j+1

while i < len(a):
    if a[i]==0:
        if a[j]==0:
            j+=1
            if j>=len(a):
                break
            continue
        a[i]=a[j]
        a[j]=0
        i+=1
    else:
        i+=1

print(a)