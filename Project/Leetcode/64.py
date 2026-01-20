# a=[-1,0,1,2,-1,-4]

# a.sort()

# b=[]

# for i in range(len(a)):
#     if i>0 and a[i]==a[i-1]:
#         continue
#     j=i+1
#     k=len(a)-1
#     while j<k:
#         if a[i]+a[j]+a[k] == 0:
#             b.append([a[i],a[j],a[k]])
#             while j < k and a[j] == a[j + 1]:
#                 j += 1
#             while j < k and a[k] == a[k - 1]:
#                 k -= 1
#             j+=1
#             k-=1
#         elif a[i]+a[j]+a[k] > 0:
#             k-=1
#         else:
#             j+=1

# print(b)

a = [-1, 0, 1, 2, -1, -4]
a.sort()  # Required for two-pointer approach

b = set()
n = len(a)

for i in range(n):
    j = i + 1
    k = n - 1

    while j < k:
        total = a[i] + a[j] + a[k]

        if total == 0:
            b.add((a[i], a[j], a[k]))  # Store as tuple to ensure uniqueness in the set
            j += 1
            k -= 1
        elif total < 0:
            j += 1
        else:
            k -= 1

# Convert set of tuples to list of lists
result = [list(triplet) for triplet in b]
print(result)
