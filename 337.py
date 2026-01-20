s1 = "parker"
s2 = "morris"
baseStr = "parser"
ans=""

parent = [i for i in range(26)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        if px < py:
            parent[py] = px
        else:
            parent[px] = py
            
for i in range(len(s1)):
    ch1=ord(s1[i])-ord("a")
    ch2=ord(s2[i])-ord("a")
    union(ch1,ch2)
    
for i in range(len(baseStr)):
    ch=chr(ord("a")+find(ord(baseStr[i]) - ord("a")))
    ans+=ch
    
print(ans)