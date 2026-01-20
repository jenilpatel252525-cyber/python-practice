a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

m=len(a)
n=len(a[0])

i=0
j=0

b=[[0] * n for  _ in range(m)]

for i in range(m):
    for j in range(n):
        count=0
        sum=0
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if 0 <=k <m and 0 <=l <n:
                    sum+=a[k][l]
                    count+=1
        b[i][j]=sum//count

print(b)