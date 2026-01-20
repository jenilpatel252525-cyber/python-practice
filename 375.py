s = "111111"

curr=0

ans=0

for i in s:
    if i=="1":
        curr+=1
    else:
        ans+=(curr*(curr+1))//2
        curr=0
else:
    ans+=(curr*(curr+1))//2
    
print(ans)