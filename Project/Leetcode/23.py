a=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

i=0
j=0
count=0

while i<len(a):
    b=a[i]
    if i==0:
        c=a[i+1]
        if j==0:
            if b[j]==1 and b[j+1]==1 and c[j]==1:
                count=count+2
            elif b[j]==1 and b[j+1]==1:
                count=count+3
            elif b[j]==1 and c[j]==1:
                count=count+3
            elif b[j]==1:
                count=count+4
                break
        elif j==len(b)-1:
            if b[j]==1 and b[j-1]==1 and c[j]==1:
                count=count+2
            elif b[j]==1 and b[j-1]==1:
                count=count+3
            elif b[j]==1 and c[j]==1:
                count=count+3
            elif b[j]==1:
                count=count+4
                break
        else:
            if b[j]==1 and b[j-1]==1 and b[j+1]==1 and c[j]==1:
                count=count+1
            elif b[j]==1 and b[j-1]==1 and b[j+1]==1:
                count=count+2
            


