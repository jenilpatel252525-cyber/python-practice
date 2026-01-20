# a= ["eat","tea","tan","ate","nat","bat"]
# b={}
# d=[]
# for i in a:
#     c={}
#     for j in i:
#         if j in c:
#             c[j]+=1
#         else:
#             c[j]=1
#     d.append(c)

a = ["eat", "tea", "tan", "ate", "nat", "bat"]
b = {}

for word in a:
    key = ''.join(sorted(word))  # sort the letters
    if key in b:
        b[key].append(word)
    else:
        b[key] = [word]

print(list(b.values()))
