s = "abccbabcdcb"
n = len(s)
l=1
ans=(0,0)

dp = [[0] * n for _ in range(n)]

for i in range(len(s)):
    for j in range(len(s)):
        if i==j:
            dp[i][j]=1
        else:
            dp[i][j]=0
            
for length in range(1,n):
    for i in range(n-length):
        j=i+length
        if s[i]==s[j]:
            if i+1 > j-1:
                dp[i][j]=dp[i+1][j-1]+2
            else:
                if dp[i+1][j-1]>0:
                    dp[i][j]=dp[i+1][j-1]+2
            if dp[i][j]>l:
                l=dp[i][j]
                ans=i,j
            
start,end=ans

print(s[start:end+1])











s = "forgeeksskeegforabcxyzyxcq"
n = len(s)

# dp[i][j] = True if s[i..j] is palindrome
dp = [[False] * n for _ in range(n)]

start = 0
max_len = 1

# length 1 substrings
for i in range(n):
    dp[i][i] = True

# length 2 substrings
for i in range(n-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = True
        start = i
        max_len = 2

# length >= 3 substrings
for length in range(3, n+1):   # substring length
    for i in range(n-length+1):
        j = i + length - 1
        if s[i] == s[j] and dp[i+1][j-1]:
            dp[i][j] = True
            if length > max_len:
                start = i
                max_len = length

print(s[start:start+max_len])
