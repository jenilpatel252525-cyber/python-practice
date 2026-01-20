w=4

val=[1,2,3]

wt=[4,5,1]

dp=[0]*(w+1)

for i in range(len(wt)):
    for j in range(w,wt[i]-1,-1):
        k=j-wt[i]
        dp[j]=max(dp[j],val[i]+dp[k])
        
print(dp)