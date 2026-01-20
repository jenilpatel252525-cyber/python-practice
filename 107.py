a=[7,6,4,3,1]

profit=0

curr=0

start=0

for i in range(1,len(a)):
    if a[i]>=a[i-1] and i<len(a)-1:
        continue
    if i==len(a)-1 and a[i]>=a[i-1]:
        curr=a[i]-a[start]
    else:
        curr=a[i-1]-a[start]
    profit+=curr
    start=i
        
print(profit)




a = [7, 6, 4, 3, 1]
profit = 0

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        profit += a[i] - a[i - 1]

print(profit)  # Output: 0
