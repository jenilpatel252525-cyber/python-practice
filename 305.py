bottom="AAAA"

allowed=["AAB","AAC","BCD","BBE","DEF"]

s={}

for i in allowed:
    if i[:2] in s:
        s[i[:2]].append(i[2])
    else:
        s[i[:2]]=[i[2]]
        
def Pyramid(curr,next,i):
    if len(curr)==1:
        return True
    if i>len(curr)-2:
        return Pyramid(next,"",0)
    if curr[i:i+2] in s:
        a=s[curr[i:i+2]]
        for j in a:
            if Pyramid(curr,next+j,i+1):
                return True
    return False

print(Pyramid(bottom,"",0))












bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]

# build mapping: pair -> list of possible tops
s = {}
for t in allowed:
    key = t[:2]
    if key in s:
        s[key].append(t[2])
    else:
        s[key] = [t[2]]

# manual cache: maps curr -> True/False
cache = {}

def Pyramid(curr, next, i):
    # base: single block
    if len(curr) == 1:
        return True

    # check cache only when starting to evaluate a full 'curr' (i == 0)
    if i == 0 and curr in cache:
        return cache[curr]

    # finished scanning current row -> move to next row
    if i > len(curr) - 2:
        # compute result for 'next'
        res = Pyramid(next, "", 0)
        if i == 0:
            cache[curr] = res
        return res

    pair = curr[i:i+2]
    if pair in s:
        for ch in s[pair]:
            if Pyramid(curr, next + ch, i + 1):
                if i == 0:
                    cache[curr] = True
                return True

    # no choice succeeded
    if i == 0:
        cache[curr] = False
    return False

print(Pyramid(bottom, "", 0))
# optional: inspect cache
# print("cache:", cache)









from collections import defaultdict
from functools import lru_cache

bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]

s = defaultdict(list)
for t in allowed:
    s[t[:2]].append(t[2])

@lru_cache(None)
def can_build(curr):
    if len(curr) == 1:
        return True
    if len(curr) == 0:
        return False   # explicit guard

    n = len(curr)

    def backtrack(i, partial):
        if i == n - 1:
            return can_build(partial)
        pair = curr[i:i+2]
        if pair not in s:
            return False
        for ch in s[pair]:
            if backtrack(i + 1, partial + ch):
                return True
        return False

    return backtrack(0, "")

print(can_build(bottom))
