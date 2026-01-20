n="123498765"
j=0
m=float('inf')
idx=-1

for i in range(len(n)-1):
    if int(n[i])<int(n[i+1]):
        j=i
        
if j!=0:
    for i in range(j+1,len(n)):
        if int(n[i])>int(n[j]) and int(n[i])<m:
            m=int(n[i])
            idx=i
            
t=""

if idx+1<len(n):
    t+=n[:j]+n[idx]+n[j+1:idx]+n[j]+n[idx+1:]
else:
    t+=n[:j]+n[idx]+n[j+1:idx]+n[j]
    
print(t)

p=j+1
q=len(n)-1

temp=list(t)

while p<q:
    temp[p],temp[q]=temp[q],temp[p]
    p+=1
    q-=1
    
print(int("".join(temp)))