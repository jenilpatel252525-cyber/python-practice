s = "abcda"

queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]

ans=[]

def isPalindrome(start,end,count):
    curr=s[start:end+1]
    i=0
    j=len(curr)-1
    while i<=j:
        if curr[i]==curr[j]:
            i+=1
            j-=1
        else:
            if count>0:
                i+=1
                j-=1
                count-=1
            else:
                return False
    return True

for i in range(len(queries)):
    if isPalindrome(queries[i][0],queries[i][1],queries[i][2]):
        ans.append(True)
    else:
        ans.append(False)
        
print(ans)










s = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]

# Step 1: Build prefix parity mask
prefix = [0]
for ch in s:
    prefix.append(prefix[-1] ^ (1 << (ord(ch) - ord('a'))))

ans = []

# Step 2: Process queries
for l, r, k in queries:
    mask = prefix[r + 1] ^ prefix[l]
    odd = bin(mask).count("1")
    ans.append(odd // 2 <= k)

print(prefix)
