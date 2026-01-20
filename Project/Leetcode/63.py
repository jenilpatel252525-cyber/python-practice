# a=[1,8,6,2,5,4,8,3,7]

# p={}

# s=set()

# for i in range(len(a)):
#     p[i]=a[i]

# sorted_by_value = dict(sorted(p.items(), key=lambda item: item[1]))

# ma=len(a)-1
# mi=0
# ans=0

# for key,value in sorted_by_value.items():
#     dis=max(ma-key,key-mi)
#     ans=max(ans,value*dis)
#     s.add(key)
#     while ma in s:
#         ma-=1
#     while mi in s:
#         mi+=1

# print(ans)

a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0
right = len(a) - 1
max_area = 0

while left < right:
    height = min(a[left], a[right])
    width = right - left
    area = height * width
    max_area = max(max_area, area)

    # Move the shorter side
    if a[left] < a[right]:
        left += 1
    else:
        right -= 1

print(max_area)
