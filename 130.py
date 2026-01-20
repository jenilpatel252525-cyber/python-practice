a=[2,3,4,5]

pre=[]

suf=[]

ans=[]

k=1

for i in a:
    k*=i
    pre.append(k)
    
k=1
    
for i in range(len(a)-1,-1,-1):
    k*=a[i]
    suf.insert(0,k)
    
# for i in range(len(a)-1, -1, -1):
#     k *= a[i]
#     suf.append(k)
# suf.reverse()
    
ans.append(suf[1])

for i in range(1,len(a)-1):
    ans.append(pre[i-1]*suf[i+1])
    
ans.append(pre[len(a)-2])

print(ans)










a = [2, 3, 4, 5]
n = len(a)
ans = [1] * n

# Step 1: Multiply with prefix products
prefix = 1
for i in range(n):
    ans[i] = prefix
    prefix *= a[i]

# Step 2: Multiply with suffix products
suffix = 1
for i in range(n - 1, -1, -1):
    ans[i] *= suffix
    suffix *= a[i]

print(ans)