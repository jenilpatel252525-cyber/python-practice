a = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1]
]
sr = 1
sc = 1
color = 2

i=0
j=0

b=[[sr,sc]]

a[sr][sc]=color

# while len(b)>0:
#     sr, sc = b.pop(0)
#     while i<len(a):
#         while j<len(a[0]):
#             if a[i][j]==1:
#                 if 0<=sr-1<len(a) and 0<=sr+1<len(a) and 0<=sc-1<len(a[0]) and 0<=sc+1<len(a[0]):
#                     if (i,j)==(sr-1,sc) or (i,j)==(sr+1,sc) or (i,j)==(sr,sc-1) or (i,j)==(sr,sc+1):
#                         a[i][j]=color
#                         b.append([i,j])
#                         print(b)
#             j+=1
#         i+=1
#         j=0
#     i=0
    
while len(b) > 0:
    sr, sc = b.pop(0) 
    for i, j in [(sr-1, sc), (sr+1, sc), (sr, sc-1), (sr, sc+1)]:
        if 0 <= i < len(a) and 0 <= j < len(a[0]) and a[i][j] == 1:
            a[i][j] = color
            b.append([i, j])

print(a)