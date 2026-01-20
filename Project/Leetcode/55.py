# a=[1,1,1,1,1,1,100]

# k=3

# c=0

# s={}

# for i in range(len(a)):
#     c+=a[i]
#     s[c]=i

# c=c/k

# d=float('inf')

# j=0

# x=0

# start=0

# count=0

# flag=False

# b=[]

# m=0

# while count<k:
#     if count==0:
#         for key,value in s.items():
#             t=abs(c-key)
#             if t<d:
#                 d=t
#                 j=value
#                 x=key
#         count+=1
#         b.append(x)
#         d=float('inf')
#     else:
#         start=j+1
#         x1=x
#         # print(start)
#         for key,value in s.items():
#             # print(value)
#             if value==start:
#                 flag=True
#             if flag:
#                 # print(key)
#                 t=abs(key-x1-c)
#                 if t<d:
#                     d=t
#                     j=value
#                     x=key
#         flag=False
#         count+=1
#         b.append(x)
#         d=float('inf')

# for y in range(len(b)):
#     if y==0:
#         m=b[y]
#     else:
#         m=max(m,b[y]-b[y-1])

# print(m)
# print(b)


def is_possible(a, k, max_sum):
    count = 1
    current = 0
    for num in a:
        if current + num > max_sum:
            count += 1
            current = num
            if count > k:
                return False
        else:
            current += num
    return True

def split_array(a, k):
    low = max(a)
    high = sum(a)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(a, k, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

a = [7, 2, 5, 10, 8]
k = 2
print(split_array(a, k))  # Output: 18




