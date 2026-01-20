s = "abcabcd"

left = 0
right = 0
start = 0
count = 0
seen = set()  # store tuples (start_char, end_char)

while right < len(s) and left < len(s):
    start = right
    left = right
    right = left + 1

    while right < len(s) and (ord(s[right]) - ord(s[left])) % 26 == 1:
        left += 1
        right += 1

    # substring s[start:left+1] is a valid wraparound segment
    # add all substrings within that segment by (first_char, last_char)
    for i in range(start, left + 1):
        seen.add((s[i], s[left]))  # first & last char uniquely identify this pattern

    n = left - start + 1
    count += (n * (n + 1)) // 2
    # move forward
    left = right

print("Total substrings (with duplicates):", count)
print("Unique substrings (by start-end pair):", len(seen))
print("Unique pairs:", seen)









dp = [0]*26
k = 0
for i in range(len(s)):
    if i>0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
        k += 1
    else:
        k = 1
    dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], k)

print(sum(dp))