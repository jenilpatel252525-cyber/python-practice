n = 4
a = []        # stores all valid boards
curr = []     # stores positions like (i, j)
cols = set()  # columns occupied
diag1 = set() # r - c → for \ diagonals
diag2 = set() # r + c → for / diagonals

def isvalid(i):
    if i == n:
        a.append(curr[:])   # found one valid placement
        return

    for j in range(n):
        if j in cols or (i - j) in diag1 or (i + j) in diag2:
            continue

        # Choose
        curr.append((i, j))
        cols.add(j)
        diag1.add(i - j)
        diag2.add(i + j)

        # Explore
        isvalid(i + 1)

        # Backtrack
        curr.pop()
        cols.remove(j)
        diag1.remove(i - j)
        diag2.remove(i + j)

isvalid(0)
print("Total solutions:", len(a))

for board in a:
    print(board)