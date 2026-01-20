s = "aabbaa"
ans = []

def ispalindrom(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def palindrom(start, path):
    if start == len(s):
        ans.append(path[:])   # copy
        return
    for l in range(1, len(s) - start + 1):   # correct range
        part = s[start:start+l]
        if ispalindrom(part):
            palindrom(start + l, path + [part])

palindrom(0, [])
print(ans)











from functools import lru_cache

s = "aabbaa"
ans = []

@lru_cache(None)   # cache results of palindrome check
def ispalindrom(subs):
    i, j = 0, len(subs) - 1
    while i <= j:
        if subs[i] != subs[j]:
            return False
        i += 1
        j -= 1
    return True

def palindrom(start, path):
    if start == len(s):
        ans.append(path[:])
        return
    for l in range(1, len(s) - start + 1):
        part = s[start:start+l]
        if ispalindrom(part):     # now cached
            palindrom(start + l, path + [part])

palindrom(0, [])
print(ans)