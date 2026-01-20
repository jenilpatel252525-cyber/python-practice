n=10

k=5

count=0

ans=[]

i=1

while count<k:
    ans.append(i)
    count+=1
    if count>=k:
        break
    ans.append(n-i+1)
    count+=1
    i+=1
    
remaining=n-len(ans)
    
if i==ans[-1]:
    while remaining>0:
        i+=1
        ans.append(i)
        remaining-=1
else:
    while remaining>0:
        ans.append(n-i+1)
        i+=1
        remaining-=1
    
print(ans)