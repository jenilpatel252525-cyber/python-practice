n=3
top=0
bottom=n-1
left=0
right=n-1
a=[[0 for _ in range(n)] for _ in range(n)]
count=1

while left<=right and top<=bottom:
    for i in range(left,right+1):
        a[top][i]=count
        count+=1
    top+=1
    
    for i in range(top,bottom+1):
        a[i][right]=count
        count+=1
    right-=1
    
    if top<=bottom:
        for i in range(right,left-1,-1):
            a[bottom][i]=count
            count+=1
        bottom-=1
    
    if left<=right:
        for i in range(bottom,top-1,-1):
            a[i][left]=count
            count+=1
        left+=1
        
print(a)