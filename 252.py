s = "1126201"

def numDecodings(s: str) -> int:
    if not s or s[0] == "0":
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1   # empty string
    dp[1] = 1   # first char already checked not zero
    
    for i in range(2, n + 1):
        # Single digit decode (must be 1–9)
        if s[i-1] != "0":
            dp[i] += dp[i-1]
        
        # Two digit decode (must be 10–26)
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]

# ---- Testing ----
print(numDecodings("1121"))     # 5
print(numDecodings("11212"))    # 8
print(numDecodings("112120"))   # 5
print(numDecodings("1121201"))  # 5
print(numDecodings("11262"))    # 5