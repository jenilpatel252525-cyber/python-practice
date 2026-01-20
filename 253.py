s = "255255"

l=len(s)

dp=[0]*3

for i in range(3):
    curr=1
    used=(i+1)*curr
    rem=l-used
    while curr<4 and rem>=4-curr and rem/(4-curr) <= 3:
        dp[i]=curr
        curr+=1
        used=(i+1)*curr
        rem=l-used
        if curr==4 and rem==0:
            dp[i]+=1
            
print(dp)














def restore_ip_addresses(s):
    res = []

    def backtrack(start, path):
        # If 4 groups are formed
        if len(path) == 4:
            if start == len(s):  # all chars used
                res.append('.'.join(path))
            return
        
        # Try lengths 1,2,3 for next group
        for l in range(1, 4):
            if start + l > len(s):  # exceed string length
                continue
            part = s[start:start+l]
            # No leading zeros unless single '0'
            if part[0] == '0' and l > 1:
                continue
            # Value <= 255
            if int(part) > 255:
                continue
            backtrack(start+l, path + [part])
    
    backtrack(0, [])
    return res

# Example usage:
s = "25525511135"
print(restore_ip_addresses(s))