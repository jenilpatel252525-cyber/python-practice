# a=[[1,3],[2,6],[8,10],[15,18]]

# b=[]

# c=[]

# i=0

# while i < len(a):
#     if i==len(a)-1:
#         b.append(a[i])
#         i+=1
#     elif a[i][1] >= a[i+1][0]:
#         c.append(a[i][0])
#         c.append(a[i+1][1])
#         b.append(c)
#         c=[]
#         i+=2
#     else:
#         b.append(a[i])
#         i+=1
        
# print(b)

a = [[1, 3], [2, 6], [8, 10], [15, 18]]
a.sort()  # Ensure intervals are sorted by start time

b = []  # Result list
i = 0

while i < len(a):
    # Start of the current merged interval
    start = a[i][0]
    end = a[i][1]
    
    # Merge all overlapping intervals
    while i + 1 < len(a) and end >= a[i + 1][0]:
        end = max(end, a[i + 1][1])
        i += 1
    
    # Add the merged interval
    b.append([start, end])
    i += 1

print(b)

# a = [[1,3],[2,6],[8,10],[15,18]]
# a.sort()
# b = [a[0]]

# for i in range(1, len(a)):
#     if a[i][0] <= b[-1][1]:  # overlap
#         b[-1][1] = max(b[-1][1], a[i][1])
#     else:
#         b.append(a[i])

# print(b)