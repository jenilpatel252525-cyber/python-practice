from collections import defaultdict

s = "CONTEST IS COMING"

d=defaultdict(list)

a=s.split(" ")

length=[len(i) for i in a]

res=[]

for i in range(len(a)-1):
    if length[i]<length[i+1]:
        res.append(length[i+1]-length[i])
    else:
        res.append(0)
        
res.append(0)
        
b=[]

for i in range(len(a)):
    b.append([])
    for j in range(len(a[i])):
        b[-1].append(a[i][j])
    if res[i]>0:
        for k in range(res[i]):
            b[-1].append(" ")

for i in b:
    for j in range(len(i)):
        d[j].append(i[j])
        
l=list(d.values())

ans=[]

for i in l:
    ans.append("".join(i))
    
print(ans)










s = "CONTEST IS COMING"
words = s.split()

max_len = max(len(w) for w in words)

ans = []
for col in range(max_len):
    temp = []
    for w in words:
        if col < len(w):
            temp.append(w[col])
        else:
            temp.append(" ")
    ans.append("".join(temp).rstrip())

print(ans)
