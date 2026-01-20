s = "zab"

base = "abcdefghijklmnopqrstuvwxyz"
used = set()
start = 0
count = 0

for i in range(len(s)):
    curr = s[i]
    if curr in used:
        continue
    else:
        used.add(curr)

    for j in range(i + 1, len(s)):
        # Check if s[j] continues the wraparound from s[j - 1]
        if (ord(s[j]) - ord(s[j - 1])) % 26 == 1:
            curr += s[j]
            used.add(curr)
        else:
            break

print("Unique substrings in wraparound:", used)
print("Count:", len(used))

        
        
        
        
        
        
def findSubstringInWraproundString(s):
    dp = [0] * 26  # dp[i]: max length of valid substring ending with chr(i + ord('a'))
    k = 0  # current length of valid substring

    for i in range(len(s)):
        if i > 0 and ((ord(s[i]) - ord(s[i-1])) % 26 == 1):
            k += 1
        else:
            k = 1

        index = ord(s[i]) - ord('a')
        dp[index] = max(dp[index], k)

    return sum(dp)
