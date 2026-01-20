n = 4
m = 3
e = 5
a = {(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)}

b = {}  # Stores node: color
elements = [i + 1 for i in range(m)]

def isAvail(i, j, arrays):
    c = set()
    for u, v in a:
        if u == i and v not in c:
            if j in arrays[v - 1]:
                arrays[v - 1].remove(j)
            c.add(v)
        elif v == i and u not in c:
            if j in arrays[u - 1]:
                arrays[u - 1].remove(j)
            c.add(u)

def colours(arrays, b, j=1):
    if j > n:
        return True

    if len(arrays[j - 1]) == 0:
        return False

    for k in range(len(arrays[j - 1])):
        color = arrays[j - 1][k]
        b[j] = color

        # Make a deep copy of arrays for backtracking
        new_arrays = [row[:] for row in arrays]
        isAvail(j, color, new_arrays)

        if colours(new_arrays, b, j + 1):
            return True

        del b[j]  # Backtrack

    return False

# Start
arrays = [elements[:] for _ in range(n)]
if colours(arrays, b):
    print("Coloring possible:")
    for node in sorted(b):
        print(f"Node {node} -> Color {b[node]}")
else:
    print("No valid coloring possible.")





n = 4
m = 3
e = 5
edges = {(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)}

colors = [0] * (n + 1)  # colors[1..n] stores the assigned color (0 = unassigned)

# Convert set to adjacency list for faster lookup
graph = {i: [] for i in range(1, n+1)}
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

def isSafe(node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def solve(node):
    if node > n:
        return True  # All nodes colored

    for color in range(1, m + 1):
        if isSafe(node, color):
            colors[node] = color
            if solve(node + 1):
                return True
            colors[node] = 0  # Backtrack

    return False

if solve(1):
    print("Color assignment is possible:")
    for i in range(1, n + 1):
        print(f"Node {i} -> Color {colors[i]}")
else:
    print("No valid coloring possible with given m colors.")