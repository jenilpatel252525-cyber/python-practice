from collections import defaultdict

a = [4, 2, 2, 6, 4]
k = 6
L = 2
R = 3
x=0
count=0
s={}

for i in range(len(a)):
    if a[i]==k:
        if 1 in range(L,R+1):
            count+=1
    x=x^a[i]
    if x==k:
        if i+1 in range(L,R+1) and i > 0:
            count+=1
            print("i")
    s[i]=x

j=0
x2=0
flag=False
start=0

while j<len(s):
    if s[j]==k:
        start=j
        flag=True
    if flag:
        x2=x2^s[j]
        if x2==0 and j-start+1 in range(L,R+1):
            count+=1
            print("j")
            flag=False
    j+=1

print(count)

# from collections import defaultdict

# def count_xor_subarrays_in_range(a, k, L, R):
#     prefix_xor = [0] * (len(a) + 1)
    
#     # Step 1: Build prefix XOR
#     for i in range(len(a)):
#         prefix_xor[i + 1] = prefix_xor[i] ^ a[i]
    
#     count = 0
#     freq = defaultdict(int)

#     # Step 2: Traverse from left to right
#     for i in range(1, len(a) + 1):
#         # Step 2a: Check all possible window sizes ending at i-1
#         for length in range(L, R + 1):
#             start = i - length
#             if start >= 0:
#                 required = prefix_xor[i] ^ k
#                 if prefix_xor[start] == required:
#                     count += 1
#         # Store current prefix XOR
#         freq[prefix_xor[i]] += 1

#     return count

# # Example
# a = [4, 2, 2, 6, 4]
# k = 6
# L = 2
# R = 3
# print(count_xor_subarrays_in_range(a, k, L, R))  # Output: 2
