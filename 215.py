price   = [3, 5, 7, 2]
special = [
    [1, 1, 0, 0, 7],   # Offer 1: 1A + 1B for $7  (vs 3+5 = 8) small saving
    [0, 2, 1, 0, 15],  # Offer 2: 2B + 1C for $15 (vs 2*5+7=17) good saving
    [2, 0, 1, 1, 14],  # Offer 3: 2A + 1C + 1D for $14 (vs 3+3+7+2=15) small saving
    [3, 2, 1, 2, 25],  # Offer 4: bundle 3A+2B+1C+2D for $25 (vs 3*3+2*5+7+4=30) big saving
    [0, 0, 2, 3, 18],  # Offer 5: 2C+3D for $18 (vs 2*7+3*2=20) moderate saving
    [1, 1, 1, 1, 15]   # Offer 6: 1 of each for $15 (vs 3+5+7+2=17) saving
]
needs   = [3, 3, 2, 2]   # Need 3A, 3B, 2C, 2D

ans=float("inf")

def remaining(needs,offer):
    ans=[]
    for x,y in zip(needs,offer[:4]):
        if x-y<0:
            return []
        ans.append(x-y)
    return ans

for offer in special:
    rem=remaining(needs,offer)
    if len(rem)<=0:
        continue
    cost=0
    for a,b in zip(rem,price):
        cost+=a*b
    total=cost+offer[-1]
    ans=min(ans,total)
    
print(ans)







from functools import lru_cache

price   = [3, 5, 7, 2]
special = [
    [1, 1, 0, 0, 7],
    [0, 2, 1, 0, 15],
    [2, 0, 1, 1, 14],
    [3, 2, 1, 2, 25],
    [0, 0, 2, 3, 18],
    [1, 1, 1, 1, 15]
]
needs   = [3, 3, 2, 2]

@lru_cache(None)
def dfs(needs):
    # cost without any offer = direct purchase
    cost = sum(n * p for n, p in zip(needs, price))
    
    # try each special
    for offer in special:
        new_needs = []
        for n, o in zip(needs, offer[:-1]):
            if n < o:   # can't use this offer
                break
            new_needs.append(n - o)
        else:
            cost = min(cost, offer[-1] + dfs(tuple(new_needs)))
    return cost

print(dfs(tuple(needs)))  # ✅ prints 37