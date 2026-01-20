a=[1,2,5,6,8]

total=25

count=float('inf')

temp=0

memo = {}  # key: (i, total2), value: min coins for that subproblem

def coin(i,total2,temp):
    global count
    if total2==0:
        count=min(count,temp)
        return
    
    if (i, total2) in memo and memo[(i, total2)] <= temp:
        return
    
    memo[(i, total2)] = temp
    
    for i in range(i,-1,-1):
        if a[i]>total2:
            continue
        k=total2//a[i]
        l=total2 % a[i]
        temp+=k
        coin(i-1,l,temp)
        temp-=k
        
coin(len(a)-1,total,temp)
        
print(count)




a = [1, 2, 5, 6, 8]
total = 12

# Initialize DP array where dp[i] = min coins to make amount i
dp = [float('inf')] * (total + 1)
dp[0] = 0  # Base case: 0 coins needed to make 0

# Fill dp table
for coin in a:
    for amt in range(coin, total + 1):
        dp[amt] = min(dp[amt], dp[amt - coin] + 1)

# Output the result
print(dp[total] if dp[total] != float('inf') else -1)