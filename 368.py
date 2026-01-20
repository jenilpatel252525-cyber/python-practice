def checkIfCanBreak(s1: str, s2: str) -> bool:
    a = sorted(s1)
    b = sorted(s2)
    
    ge = le = True
    for i in range(len(a)):
        if a[i] < b[i]:
            ge = False
        if a[i] > b[i]:
            le = False
    
    return ge or le





class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        
        # build frequency arrays
        for c in s1:
            cnt1[ord(c) - 97] += 1
        for c in s2:
            cnt2[ord(c) - 97] += 1
        
        # check if s2 can break s1
        carry = 0
        ok1 = True
        for i in range(26):
            carry += cnt1[i] - cnt2[i]
            if carry < 0:
                ok1 = False
                break
        
        # check if s1 can break s2
        carry = 0
        ok2 = True
        for i in range(26):
            carry += cnt2[i] - cnt1[i]
            if carry < 0:
                ok2 = False
                break
        
        return ok1 or ok2












class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        
        for c in s1:
            cnt1[ord(c) - 97] += 1
        for c in s2:
            cnt2[ord(c) - 97] += 1
        
        carry1 = carry2 = 0
        ok1 = ok2 = True
        
        for i in range(26):
            diff = cnt1[i] - cnt2[i]
            
            carry1 += diff      # s1 breaks s2
            carry2 -= diff      # s2 breaks s1
            
            if carry1 < 0:
                ok1 = False
            if carry2 < 0:
                ok2 = False
            
            # early exit if both impossible
            if not ok1 and not ok2:
                return False
        
        return True
