# s="aaaa"

# a={}

# flag=True

# length=0

# for i in range(len(s)):
#     if s[i] in a:
#         length=max(length,i-a[s[i]])
#         a[s[i]]=i
#         flag=False
#     else:
#         a[s[i]]=i

# if flag:
#     length=len(a)

# print(length)

s = "abba"

last_index = {}
start = 0
max_length = 0

for i, ch in enumerate(s):
    if ch in last_index and last_index[ch] >= start:
        start = last_index[ch] + 1
    max_length = max(max_length, i - start + 1)
    last_index[ch] = i

print(max_length)
