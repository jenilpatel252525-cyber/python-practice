a=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

# b=[]
# d=[]

# c=a[0]

# i=0

# while i<len(a):
#     d.append(a[i])
#     s=sum(d)
#     if s>=c:
#         b=d
#         c=s
#     else:
#         d.pop()
#         d=[]
    
#     if len(d)>1:
#         p=d[0]
#         d.remove(d[0])
#         s=sum(d)
#         if s>=c:
#             b=d
#             c=s
#         else:
#             d.insert(0,p)
    
#     i+=1

max_sum = current_sum = a[0]

for i in range(1, len(a)):
    current_sum = max(a[i], current_sum + a[i])
    max_sum = max(max_sum, current_sum)



