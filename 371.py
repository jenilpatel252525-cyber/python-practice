favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]

from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # Step 1: assign bit index to each company
        company_id = {}
        bit = 0
        for companies in favoriteCompanies:
            for c in companies:
                if c not in company_id:
                    company_id[c] = bit
                    bit += 1
        
        # Step 2: build bitmask for each person
        masks = []
        for companies in favoriteCompanies:
            mask = 0
            for c in companies:
                mask |= 1 << company_id[c]
            masks.append(mask)
        
        n = len(masks)
        
        # Step 3: sort people by number of bits (company count)
        order = sorted(range(n), key=lambda i: masks[i].bit_count())
        
        res = []
        
        # Step 4: subset check using bitmask
        for i in range(n):
            idx = order[i]
            is_subset = False
            
            for j in range(i + 1, n):
                if masks[idx] & masks[order[j]] == masks[idx]:
                    is_subset = True
                    break
            
            if not is_subset:
                res.append(idx)
        
        return sorted(res)









from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        
        # Convert each person's list to a set
        sets = [set(fc) for fc in favoriteCompanies]
        
        # Sort indices by size of company list
        order = sorted(range(n), key=lambda i: len(sets[i]))
        
        res = []
        
        for i in range(n):
            idx = order[i]
            is_subset = False
            
            # Only check against people with strictly larger sets
            for j in range(i + 1, n):
                if sets[idx].issubset(sets[order[j]]):
                    is_subset = True
                    break
            
            if not is_subset:
                res.append(idx)
        
        return sorted(res)