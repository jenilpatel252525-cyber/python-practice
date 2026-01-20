a=[1,10,15,5,2,7]

dp=[0]*(len(a))

dp[0],dp[1],dp[2]=a[0],a[1],a[2]+a[0]

for i in range(3,len(a)):
    dp[i]=max(a[i]+dp[i-2],a[i]+dp[i-3])
    
# print(dp)





cost = [1,100,1,1,1,100,1,1,100,1]

dp=[0]*(len(cost))

dp[0],dp[1]=cost[0],cost[1]

for i in range(2,len(cost)):
    dp[i]=min(dp[i-1]+cost[i],dp[i-2]+cost[i])
    
print(dp)