a=[-2,1,-3,4,-1,2,1,-5,4]

sum3=-float('inf')
sum1=0
sum2=0
s=[0] * (len(a)+1)
j=0
k=0

for i in range(len(a)):
    s[i+1]=s[i]+a[i]
    sum1+=a[i]
    while j<i:
        if sum1>=sum3:
            sum3=sum1
            k=j
        sum1-=a[j]
        j+=1
    j=k
    if i>0:
        sum1=s[i+1]-s[j]
    
print(sum3)

# a = [5, 4, -1, 7, 8]

# max_sum = current_sum = a[0]

# for i in range(1, len(a)):
#     current_sum = max(a[i], current_sum + a[i])
#     max_sum = max(max_sum, current_sum)

# print(max_sum)  # Output: 23