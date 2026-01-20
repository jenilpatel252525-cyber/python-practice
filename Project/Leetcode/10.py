a=[1,2,3,2,1,4,5,6,3,6,5]
# a.sort()

# i=0
# b=[]

# while i<len(a)-1:
#     if a[i]==a[i+1]:
#         i=i+2
#     else:
#         b.append(a[i])
#         break
    
# print(b)

c=set()

for num in a:
    if num in c:
        c.remove(num)
        continue
    else:
        c.add(num)


print(c) 
    