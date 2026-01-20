nums = [0,1,1,1,1,1,0,0,0]

ans=0

s={}

s[0]=-1

c=0

for i in range(len(nums)):
    if nums[i]==0:
        c-=1
    else:
        c+=1
    if c in s:
        temp=s[c]
        ans=max(ans,i-temp)
    else:
        s[c]=i
        
print(ans)