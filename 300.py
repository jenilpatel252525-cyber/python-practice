from collections import deque

def check_valid_string(s: str) -> bool:
    left = deque()  # indices of '('
    star = deque()  # indices of '*'

    # 1) First pass: handle ')' greedily
    for i, ch in enumerate(s):
        if ch == "(":
            left.append(i)
        elif ch == "*":
            star.append(i)
        else:  # ch == ')'
            if left:
                left.pop()       # use a '('
            elif star:
                star.pop()       # use a '*' as ')'
            else:
                return False     # no way to match this ')'

    # 2) Second pass: match remaining '(' with '*' that come after them
    while left and star:
        if left[-1] < star[-1]:
            left.pop()
            star.pop()
        else:
            # we have a '(' that appears after every remaining '*'
            # can't match it with any star
            break

    # valid only if no unmatched '(' left
    return not left










def check_valid_string_greedy(s: str) -> bool:
    """
    Greedy range of possible open parentheses.
    low  = minimum possible '(' count
    high = maximum possible '(' count
    """
    low = high = 0
    for ch in s:
        if ch == '(':
            low += 1
            high += 1
        elif ch == ')':
            low -= 1
            high -= 1
        else:  # '*'
            low -= 1      # if '*' is ')'
            high += 1     # if '*' is '('

        if high < 0:
            return False
        if low < 0:
            low = 0

    return low == 0


# ======================================================
# 2) Two stacks (indices) approach – O(n) time, O(n) space
# ======================================================
def check_valid_string_stacks(s: str) -> bool:
    """
    Use index stacks:
    - left: indices of '('
    - star: indices of '*'
    First match ')' while scanning.
    Then match remaining '(' with '*' that appear AFTER them.
    """
    left = []  # indices of '('
    star = []  # indices of '*'

    # 1) Handle all ')' greedily
    for i, ch in enumerate(s):
        if ch == '(':
            left.append(i)
        elif ch == '*':
            star.append(i)
        else:  # ')'
            if left:
                left.pop()
            elif star:
                star.pop()    # use '*' as ')'
            else:
                return False  # cannot match this ')'

    # 2) Match remaining '(' with '*' to the right
    while left and star:
        if left[-1] < star[-1]:
            left.pop()
            star.pop()
        else:
            break

    return not left