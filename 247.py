n=6

dp=[""]*n

dp[0]+=str(1)

for i in range(1,n):
    curr=dp[i-1]
    count=1
    s=curr[0]
    ans=""
    for j in range(1,len(curr)):
        if curr[j]==s:
            count+=1
        else:
            ans+=str(count)+s
            s=curr[j]
            count=1
    ans+=str(count)+s
    dp[i]+=ans

print(dp)









def countAndSay(n: int) -> str:
    curr = "1"
    for _ in range(1, n):
        ans = ""
        count = 1
        s = curr[0]
        for j in range(1, len(curr)):
            if curr[j] == s:
                count += 1
            else:
                ans += str(count) + s
                s = curr[j]
                count = 1
        ans += str(count) + s
        curr = ans
    return curr