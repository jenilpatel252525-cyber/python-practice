a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

rows = len(a)
cols = len(a[0])
max_side = 0

def is_square(r, c, size):
    if r + size > rows or c + size > cols:
        return False
    for i in range(r, r + size):
        for j in range(c, c + size):
            if a[i][j] != "1":
                return False
    return True

# Try every top-left (i, j)
for i in range(rows):
    for j in range(cols):
        if a[i][j] == "1":
            side = 1
            while is_square(i, j, side):
                max_side = max(max_side, side)
                side += 1

print(max_side)







a = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

rows = len(a)
cols = len(a[0])
dp = [[0]*cols for _ in range(rows)]
max_side = 0

for i in range(rows):
    for j in range(cols):
        if a[i][j] == "1":
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            max_side = max(max_side, dp[i][j])

print(max_side)