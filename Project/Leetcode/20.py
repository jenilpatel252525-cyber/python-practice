a=[3,1,2,4]

i=1
max=a[0]

# while i<len(a)-1:
#     if a[i]>a[j]:
#         temp=a[i]
#         a[i]=a[j]
#         a[j]=temp
#         j+=1
#     else:
#         j+=1
#     if j>=len(a):
#         i+=1
#         j=i+1





# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#         i+=1
#     else:
#         i+=1

# a.remove(max)

# max=a[0]
# i=1
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#         i+=1
#     else:
#         i+=1

# a.remove(max)

# max=a[0]
# i=1
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#         i+=1
#     else:
#         i+=1







first=second=third=float('-inf')

for num in a:

    if num > first:
        third = second
        second = first
        first = num
    elif num > second:
        third = second
        second = num
    elif num > third:
        third = num



print(third)