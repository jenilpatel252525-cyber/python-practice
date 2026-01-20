deadends = ["0201","0101","0102","1212","2002"]

target = "0202"

from collections import deque

def neighbors(code):
    res = []
    arr = list(code)
    for i in range(4):
        digit = ord(arr[i]) - 48  # '0' -> 0
        for d in (-1, 1):
            new_digit = (digit + d) % 10
            new_code = code[:i] + chr(new_digit + 48) + code[i+1:]
            res.append(new_code)
    return res

def openLock(deadends, target):
    dead = set(deadends)
    start = "0000"
    if start in dead:
        return -1
    if target == start:
        return 0

    q = deque([(start, 0)])  # (code, steps)
    visited = {start}

    while q:
        code, steps = q.popleft()
        for nxt in neighbors(code):
            if nxt in dead or nxt in visited:
                continue
            if nxt == target:
                return steps + 1
            visited.add(nxt)
            q.append((nxt, steps +
                      1))
    return -1
