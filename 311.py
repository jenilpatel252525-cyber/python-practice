import bisect

s = "abcde"

words = ["a","bb","acd","ace"]

dp = [[] for _ in range(26)]
for i, ch in enumerate(s):
    dp[ord(ch)-97].append(i)

ans = []
for word in words:
    prev = -1
    ok = True
    for ch in word:
        arr = dp[ord(ch)-97]
        j = bisect.bisect_right(arr, prev)
        if j == len(arr):
            ok = False
            break
        prev = arr[j]
    if ok:
        ans.append(word)

print(ans)
