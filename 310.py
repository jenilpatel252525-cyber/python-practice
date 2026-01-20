from collections import Counter

order = "cba"

s = "abcd"

c=Counter(s)

so=set(order)

ss=set(s)

remain=list(ss.difference(so))

ans=""

for i in order:
    if i in c:
        ans+=c[i]*i
        
for i in remain:
    ans+=c[i]*i
    
print(ans)
















from collections import Counter

order = "cba"
s = "abcd"

count = Counter(s)
order_set = set(order)

res = []

# ordered characters
for ch in order:
    if ch in count:
        res.append(ch * count[ch])

# remaining characters
for ch in count:
    if ch not in order_set:
        res.append(ch * count[ch])

ans = "".join(res)
print(ans)
