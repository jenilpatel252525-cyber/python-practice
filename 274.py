num = "1432219"

n=len(num)

k = 3

def pick(i,j):
    m=float("inf")
    l=0
    for k in range(i,n-j):
        if int(num[k])<m:
            m=int(num[k])
            l=k
    return m,l

p=0
q=k
ans=""

for i in range(n-k):
    num1,idx=pick(p,q)
    ans+=str(num1)
    p=idx+1
    q-=1
    
print(ans)













def removeKdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # if k > 0, remove from the end
    stack = stack[:-k] if k else stack
    
    # convert to string and remove leading zeros
    result = "".join(stack).lstrip("0")
    
    return result if result else "0"









num = "1432219"
n = len(num)
k = 3

# Precompute suffix minima
suffix_min = [0]*n
suffix_idx = [0]*n

suffix_min[-1] = int(num[-1])
suffix_idx[-1] = n-1

for i in range(n-2, -1, -1):
    if int(num[i]) <= suffix_min[i+1]:
        suffix_min[i] = int(num[i])
        suffix_idx[i] = i
    else:
        suffix_min[i] = suffix_min[i+1]
        suffix_idx[i] = suffix_idx[i+1]

# Now build answer
ans = ""
p = 0
q = k

for _ in range(n - k):
    # pick smallest in window p..n-q
    digit = suffix_min[p]
    idx = suffix_idx[p]
    ans += str(digit)
    p = idx + 1
    q -= 1

print(ans)  # 1219
