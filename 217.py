pairs = [
    [5, 24],
    [15, 25],
    [27, 40],
    [50, 60],
    [1, 2],
    [2, 3],
    [3, 4],
    [6, 7],
    [8, 9],
    [9, 10],
    [11, 12],
    [20, 30],
    [31, 32]
]

pairs.sort()

count=1

end=pairs[0][1]

for pair in pairs[1:]:
    if pair[0]>end:
        count+=1
        end=pair[1]
    else:
        end=min(end,pair[1])

print(count)









pairs = [
    [5, 24],
    [15, 25],
    [27, 40],
    [50, 60],
    [1, 2],
    [2, 3],
    [3, 4],
    [6, 7],
    [8, 9],
    [9, 10],
    [11, 12],
    [20, 30],
    [31, 32]
]

# ✅ Sort by second element (end of pair)
pairs.sort(key=lambda x: x[1])

count = 0
end = float("-inf")

for pair in pairs:
    if pair[0] > end:
        count += 1
        end = pair[1]

print(count)  # ✅ 8