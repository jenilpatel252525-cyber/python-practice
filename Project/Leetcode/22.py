# a=[1,2,4]
# b=[1,2,3]

# i=0
# j=0
# count=0

# while i<len(a):
#     if b[j]>=a[i]:
#         count+=1
#         i+=1
#         j+=1
#     else:
#         j+=1
#     if j>=len(b):
#         break

# print(count)

a=[2,1,4,3]
b=[4,1,2]
c=[]
d=[]
i=0
j=0
k=1

while i<len(a):
    if j<len(b) and b[j]>=a[i]:
        c.append(b[j])
        min=c[0]
        j+=1
    elif j<len(b):
        j+=1
    if j>=len(b) and len(c)>1:
        if k>=len(c):
            d.append(min)
            b[b.index(min)]=-b[b.index(min)]
            c=[]
            i+=1
            j=0
            k=1
        else:
            if c[k] < min:
                min = c[k]
            k += 1
    elif j>=len(b) and len(c)==1:
        d.append(min)
        b[b.index(min)]=-b[b.index(min)]
        c=[]
        i+=1
        j=0
        k=1
    elif j>=len(b) and len(c)==0:
        i+=1
        j=0
        k=1

print(d)