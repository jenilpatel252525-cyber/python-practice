# a=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# i=0
# j=0

# m=len(a)
# n=len(a[0])

# s=[]

# for i in range(m):
#     for j in range(n):
#         if a[i][j]==0:
#             s.append([i,j])
            
# for cell in s:
#     for p in range(n):
#         a[cell[0]][p]=0
#     for q in range(m):
#         a[q][cell[1]]=0
        
# print(a)

a = [[0, 1, 2, 0],
     [3, 4, 5, 2],
     [1, 3, 1, 5]]

m = len(a)
n = len(a[0])

first_row_zero = any(a[0][j] == 0 for j in range(n))
first_col_zero = any(a[i][0] == 0 for i in range(m))

# Use first row and first column as flags
for i in range(1, m):
    for j in range(1, n):
        if a[i][j] == 0:
            a[i][0] = 0
            a[0][j] = 0

# Zero rows based on first column
for i in range(1, m):
    if a[i][0] == 0:
        for j in range(n):
            a[i][j] = 0

# Zero columns based on first row
for j in range(1, n):
    if a[0][j] == 0:
        for i in range(m):
            a[i][j] = 0

# Zero first row if needed
if first_row_zero:
    for j in range(n):
        a[0][j] = 0

# Zero first column if needed
if first_col_zero:
    for i in range(m):
        a[i][0] = 0

# Final result
print(a)

a = [[0, 1, 2, 0],
     [3, 4, 5, 2],
     [1, 3, 1, 5]]

m = len(a)
n = len(a[0])

zero_rows = set()
zero_cols = set()

# Step 1: Identify rows and columns that need to be zeroed
for i in range(m):
    for j in range(n):
        if a[i][j] == 0:
            zero_rows.add(i)
            zero_cols.add(j)

# Step 2: Zero out rows
for i in zero_rows:
    for j in range(n):
        a[i][j] = 0

# Step 3: Zero out columns
for j in zero_cols:
    for i in range(m):
        a[i][j] = 0

# Final result
print(a)
