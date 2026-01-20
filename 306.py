s = "ababcbacadefegdehijhklij"

# dp[c] = [first_index, last_index] for char c ('a' -> 0, ...)
dp = [[-1, -1] for _ in range(26)]

for i, ch in enumerate(s):
    idx = ord(ch) - ord("a")
    if dp[idx][0] == -1:
        dp[idx][0] = dp[idx][1] = i
    else:
        dp[idx][1] = i

# build list of intervals for characters that actually appear
intervals = []
for idx in range(26):
    start, end = dp[idx]
    if start != -1:
        intervals.append((start, end))

# sort intervals by start (number of intervals ≤ 26 so cost is tiny)
intervals.sort()

# merge intervals and collect partition sizes
ans = []
if intervals:
    cur_start, cur_end = intervals[0]
    for s_i, e_i in intervals[1:]:
        if s_i > cur_end:
            # disjoint -> finalize current partition
            ans.append(cur_end - cur_start + 1)
            cur_start, cur_end = s_i, e_i
        else:
            # overlap -> extend the current partition
            if e_i > cur_end:
                cur_end = e_i
    # finalize last partition
    ans.append(cur_end - cur_start + 1)

print(ans)  # expected: [9, 7, 8]





def partitionLabels(s):
    last = {c: i for i, c in enumerate(s)}
    
    res = []
    start = 0
    end = 0
    
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            res.append(end - start + 1)
            start = i + 1

    return res
