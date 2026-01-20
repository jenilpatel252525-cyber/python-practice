from math import gcd

class Solution:
    def simplifiedFractions(self, n: int):
        store = []
        
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if gcd(i, j) == 1:
                    store.append(f"{i}/{j}")
        
        return store

n=4