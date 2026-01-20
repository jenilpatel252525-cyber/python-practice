# a=[[1,2,3],[4,5,6],[7,8,9]]
# j=len(a)-1

# for i in range(len(a)):
#     a[0][i],a[i][j],a[j][j-i],a[j-i][0]=a[i][j],a[j][j-i],a[j-i][0],a[0][i]
        # use temp variable
# print(a)

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Transpose
for i in range(len(a)):
    for j in range(i, len(a)):
        a[i][j], a[j][i] = a[j][i], a[i][j]

# Reverse each row
for row in a:
    row.reverse()

print(a)