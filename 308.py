start = "XXRXXLXRXLXXR"

result = "XXXRXLXXRLXXR"

def swap(start,result):
    ans=""
    global next
    next=""
    for i in range(len(start)-1):
        if next=="":
            if start[i]==result[i]:
                ans+=result[i]
            else:
                if start[i:i+2]=="XL" and result[i]=="L":
                    ans+="L"
                    next="X"
                elif start[i:i+2]=="RX" and result[i]=="X":
                    ans+="X"
                    next="R"
                else:
                    return False
        elif next=="X":
            if next==result[i]:
                ans+=next
                next=""
            elif result[i]=="L" and start[i+1]=="L":
                ans+="L"
                next="X"
            else:
                return False
        else:
            if next==result[i]:
                ans+=next
                next=""
            elif result[i]=="X" and start[i+1]=="X":
                ans+="X"
                next="R"
            else:
                return False
    if next=="":
        if start[-1]==result[-1]:
            return True
        else:
            return False
    elif next==result[-1]:
        return True
    else:
        return False
    
print(swap(start,result))

















class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # Rule 1: L and R order must match
        if start.replace("X", "") != result.replace("X", ""):
            return False

        i = j = 0
        n = len(start)

        while i < n and j < n:
            # Skip X in start
            while i < n and start[i] == "X":
                i += 1
            # Skip X in result
            while j < n and result[j] == "X":
                j += 1

            if i == n or j == n:
                break

            # Rule 2 & 3: direction constraints
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False

            i += 1
            j += 1

        return True
