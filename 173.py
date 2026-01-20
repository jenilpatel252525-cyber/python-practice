total=11
limit=10
curr=0

count=0

while curr<total:
    curr+=limit
    limit-=1
    count+=1
    
if count%2==0:
    print("false")
else:
    print("true")
    
    




def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
    # If sum of all numbers < desiredTotal, no one can win
    if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
        return False
    if desiredTotal <= 0:
        return True
    
    used = [False] * (maxChoosableInteger + 1)  # index 1-based
    
    memo = {}
    
    def can_win(current_total):
        key = tuple(used)
        if key in memo:
            return memo[key]
        
        for i in range(1, maxChoosableInteger + 1):
            if not used[i]:
                # If choosing i wins immediately or forces opponent to lose
                if current_total + i >= desiredTotal or not can_win(current_total + i):
                    used[i] = True
                    memo[key] = True
                    used[i] = False
                    return True
        memo[key] = False
        return False
    
    return can_win(0)