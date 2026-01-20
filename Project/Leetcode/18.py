a=[1,2,2,2.3,4,5]

b=[8,2,6,4,4,2]

c=[]

# for i in a:
#     if a.count(i)>=1 and b.count(i)>=1 and c.count(i)==0:
#         c.append(i)


# print(c)

a1=set(a)

b1=set(b)

for i in a1:
    if i in b1:
        c.append(i)

print(c)


