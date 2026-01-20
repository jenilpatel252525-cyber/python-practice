# a=[3,1,2]

# b=[5,1,4,2,3]

# c=[]

# i=0
# j=0
# k=False

# while i<len(a):
#     if a[i]==b[j]:
#         k=True
#     if b[j]>a[i] and k:
#         c.append(b[j])
#         j=0
#         i+=1
#         k=False
#     if j==len(b)-1:
#         c.append(-1)
#         j=0
#         i+=1
#         k=False
#     else:
#         j+=1

# print(c)




a = [3, 1, 2]
b = [5, 1, 4, 2, 3]

# Step 1: Preprocess next greater elements for b
stack = []
next_greater = {}

for num in b:
    while stack and num > stack[-1]:
        top = stack.pop()
        next_greater[top] = num
    stack.append(num)

# For remaining elements with no greater on right
while stack:
    top = stack.pop()
    next_greater[top] = -1

# Step 2: Lookup for each element in a
c = []
for num in a:
    c.append(next_greater[num])

print(c)


    