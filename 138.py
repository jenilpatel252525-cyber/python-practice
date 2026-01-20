# a=[1,2,3,4,1,2,5,6]

# m=0

# start=0
# i=0

# end=len(a)-1

# while i<=end:
#     flag=False
#     while i<end and a[i]>a[i+1]:
#         flag=True
#         i+=1
#     start=i
#     if flag:
#         l=2
#     else:
#         l=1
#     i+=1
#     curr=i
#     while i<end:
#         if a[i+1]>a[curr]:
#             l+=1
#             i+=1
#             curr=i
#         elif a[i+1]<start:
#             i+=1
#             break
#         else:
#             i+=1
#             curr=i
#     m=max(m,l)
    
# print(m)





def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)




import bisect
def lengthOfLIS(nums):
    sub = []
    for num in nums:
        idx = bisect.bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num
    return len(sub)
