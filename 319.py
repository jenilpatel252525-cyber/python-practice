s = "aaa" 

shifts = [1,2,3]

suffix=shifts[:]

for i in range(len(suffix)-2,-1,-1):
    suffix[i]+=suffix[i+1]
    
ans=""
    
for i in range(len(s)):
    ch=chr(((ord(s[i])+suffix[i]-ord("a"))%26) + ord("a"))
    ans+=ch

print(ans)