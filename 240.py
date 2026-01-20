deadends = ["0201","0101","0102","1212","2002"]

target="0202"

from collections import deque

def openLock(deadends, target):
    dead = set(deadends)
    if "0000" in dead:
        return -1
    
    q = deque([("0000", 0)])
    visited = {"0000"}
    
    while q:
        state, steps = q.popleft()
        
        if state == target:
            return steps
        
        for i in range(4):  # choose wheel
            digit = int(state[i])
            for move in (-1, 1):  # turn down or up
                new_digit = (digit + move) % 10
                new_state = state[:i] + str(new_digit) + state[i+1:]
                
                if new_state not in visited and new_state not in dead:
                    visited.add(new_state)
                    q.append((new_state, steps + 1))
    
    return -1