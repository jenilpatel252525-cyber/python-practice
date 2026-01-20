citations = [0,1,3,5,6]

low=0
high=len(citations)-1
n=len(citations)
ans=0

while low<=high:
    mid=int((low+high)/2)
    count=n-mid
    if citations[mid]>=count:
        ans=count
        high=mid-1
    else:
        low=mid+1
        
print(ans)