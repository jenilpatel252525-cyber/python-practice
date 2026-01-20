s = "catsandog"

wordDict = ["og","cats","dog","sand","and","cat"]

worddict=set(wordDict)

def find(start):
    if start==len(s):
        return True
    res=False
    for l in range(1,len(s)-start+1):
        part=s[start:start+l]
        if part in worddict:
            res = res or find(start+l)
    return res

print(find(0))











memo = {}

def find(start):
    if start == len(s):
        return True
    if start in memo:       # ✅ If already computed, return saved result
        return memo[start]
    
    for l in range(1, len(s) - start + 1):
        part = s[start:start+l]
        if part in worddict and find(start+l):
            memo[start] = True   # ✅ Save result
            return True
    
    memo[start] = False
    return False