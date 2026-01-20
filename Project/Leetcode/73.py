a=[1,2,3]
b=[]

# def permutations(a,b):
    
#     j=len(a)-2
#     while j>0 and a[j]>a[j+1]:
#         j-=1
    
#     if j>=0:
#         i=len(a)-1
#         while a[i]>a[j]:
#             i-=1
        
#     a[i],a[j]=a[j],a[i]

#     left = j + 1
#     right = len(a) - 1

#     while left < right:
#         a[left], a[right] = a[right], a[left]
#         left += 1
#         right -= 1

#     while a not in b:
#         b.append(a)
#         permutations(a,b)
        
#     return(b)

# print(permutations(a,b))

def next_permutation(a):
    j = len(a) - 2
    while j >= 0 and a[j] >= a[j + 1]:
        j -= 1

    if j >= 0:
        i = len(a) - 1
        while a[i] <= a[j]:
            i -= 1
        a[i], a[j] = a[j], a[i]

    a[j + 1:] = reversed(a[j + 1:])
    return a

def permutations(a):
    a = sorted(a)  # start with smallest lex permutation
    result = [a[:]]  # store first permutation

    while True:
        curr = a[:]
        next_perm = next_permutation(curr[:])
        if next_perm == result[0]:  # back to first → stop
            break
        result.append(next_perm[:])
        a = next_perm[:]

    return result
