a=[1,1,0,1,0,1,1,1,0,0,1,0,1,1]

i=0
j=i+1
max=0
c=0

# while j<len(a):
#     if i==len(a)-1:
#         if a[i]==1 and max==0:
#             max=1
#             break
#     if a[i]==1:
#         if c==0:
#             c+=1
#         if a[j]==1:
#             c+=1
#             j+=1
#         else:
#             if c>max:
#                 max=c
#             c=0
#             i=j+1
#             j=i+1
#     else:
#         i+=1
#         j=i+1

# if c>max:
#     max=c

# print(max)

a = [1,1,0,1,0,1,1,1,0,0,1,0,1,1]

max_count = 0
current_count = 0

for num in a:
    if num == 1:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print(max_count)
