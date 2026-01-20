heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

ans = []
inpacific = set()
inatlantic = set()

# Add visited set to prevent infinite loop
def pacific(i, j, visited=set()):
    if (i, j) in inpacific:
        return True
    if (i, j) in visited:
        return False
    if i == 0 or j == 0:
        inpacific.add((i, j))
        return True

    visited.add((i, j))

    if i - 1 >= 0 and heights[i - 1][j] <= heights[i][j] and pacific(i - 1, j, visited):
        inpacific.add((i, j))
        return True
    if i + 1 < len(heights) and heights[i + 1][j] <= heights[i][j] and pacific(i + 1, j, visited):
        inpacific.add((i, j))
        return True
    if j - 1 >= 0 and heights[i][j - 1] <= heights[i][j] and pacific(i, j - 1, visited):
        inpacific.add((i, j))
        return True
    if j + 1 < len(heights[0]) and heights[i][j + 1] <= heights[i][j] and pacific(i, j + 1, visited):
        inpacific.add((i, j))
        return True

    return False

def atlantic(i, j, visited=set()):
    if (i, j) in inatlantic:
        return True
    if (i, j) in visited:
        return False
    if i == len(heights) - 1 or j == len(heights[0]) - 1:
        inatlantic.add((i, j))
        return True

    visited.add((i, j))

    if i - 1 >= 0 and heights[i - 1][j] <= heights[i][j] and atlantic(i - 1, j, visited):
        inatlantic.add((i, j))
        return True
    if i + 1 < len(heights) and heights[i + 1][j] <= heights[i][j] and atlantic(i + 1, j, visited):
        inatlantic.add((i, j))
        return True
    if j - 1 >= 0 and heights[i][j - 1] <= heights[i][j] and atlantic(i, j - 1, visited):
        inatlantic.add((i, j))
        return True
    if j + 1 < len(heights[0]) and heights[i][j + 1] <= heights[i][j] and atlantic(i, j + 1, visited):
        inatlantic.add((i, j))
        return True

    return False

def count(heights):
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if pacific(i, j, set()) and atlantic(i, j, set()):
                ans.append([i, j])

count(heights)
print(ans)