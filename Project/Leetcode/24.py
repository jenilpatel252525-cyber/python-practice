a=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
row=len(a)
col=len(a[0])

b=[[item for sublist in a for item in sublist]]

i=0
r=0
c=0
count=0

# while i<len(b):
#     if a[i]==1:
#         if r==0 and c==0:
#             if a[i+1]==1 and a[i+col]==1:
#                 count=count+2
#             elif a[i+1]==1:
#                 count=count+3
#             elif a[i+col]==1:
#                 count=count+3
#             else:
#                 count=count+4
#                 break
#             i=i+1
#             c=c+1
#             if c>=col:
#                 c=0
#                 r=r+1
#         if r==0 and c==col-1:
#             if a[i-1]==1 and a[i+col]==1:
#                 count=count+2
#             elif a[i-1]==1:
#                 count=count+3
#             elif a[i+col]==1:
#                 count=count+3
#             else:
#                 count=count+4
#                 break
#             i=i+1
#             c=c+1
#             if c>=col:
#                 c=0
#                 r=r+1
#         if r==row-1 and c==0:
#             if a[i+1]==1 and a[i-col]==1:
#                 count=count+2
#             elif a[i+1]==1:
#                 count=count+3
#             elif a[i-col]==1:
#                 count=count+3
#             else:
#                 count=count+4
#                 break
#             i=i+1
#             c=c+1
#             if c>=col:
#                 c=0
#                 r=r+1
#         if r==row-1 and c==col-1:
#             if a[i-1]==1 and a[i-col]==1:
#                 count=count+2
#             elif a[i-1]==1:
#                 count=count+3
#             elif a[i-col]==1:
#                 count=count+3
#             else:
#                 count=count+4
#                 break
#             i=i+1
#             c=c+1
#             if c>=col:
#                 c=0
#                 r=r+1
#         if r==0:
#             if a[i-1]==1 and a[i+col]==1 and a[i+1]==1:
#                 count=count+1
            



def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                # Check top
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 1
                # Check bottom
                if r < rows - 1 and grid[r+1][c] == 1:
                    perimeter -= 1
                # Check left
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 1
                # Check right
                if c < cols - 1 and grid[r][c+1] == 1:
                    perimeter -= 1
    return perimeter




