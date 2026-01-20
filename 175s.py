matchsticks = [1,1,1,1,2,2,2,2,3,3,3,3]

matchsticks.sort()

total = sum(matchsticks)

def find_leq(arr, target, i, used):
    left, right = 0, i
    result = -1  # Store best candidate ≤ target

    while left <= right:
        mid = (left + right) // 2
        if not used[mid] and arr[mid] <= target:
            result = mid  # valid candidate
            left = mid + 1  # look for larger valid candidate on the right
        else:
            right = mid - 1

    return result  # returns -1 if no such element

def issquare():
    if total % 4 != 0:
        return False

    target = total // 4
    used = [False] * len(matchsticks)

    for _ in range(4):  # try to form 4 equal sides
        curr = target
        i = len(matchsticks) - 1

        while curr > 0:
            res = find_leq(matchsticks, curr, i, used)
            if res == -1:
                return False
            curr -= matchsticks[res]
            used[res] = True  # mark as used
            i = res - 1  # search to the left of last used element

    return True

print(issquare())







def makesquare(matchsticks):
    total = sum(matchsticks)
    if total % 4 != 0:
        return False

    side_length = total // 4
    matchsticks.sort(reverse=True)  # sort descending for pruning
    sides = [0] * 4

    def dfs(index):
        if index == len(matchsticks):
            # Check if all sides are exactly equal
            return all(side == side_length for side in sides)

        for i in range(4):
            if sides[i] + matchsticks[index] <= side_length:
                sides[i] += matchsticks[index]
                if dfs(index + 1):
                    return True
                sides[i] -= matchsticks[index]  # backtrack

            # Optimization: if this side is still 0 after attempt, no need to try other empty sides
            if sides[i] == 0:
                break

        return False

    return dfs(0)


# Test case you asked about
matchsticks = [1,1,1,1,2,2,2,2,3,3,3,3]
print(makesquare(matchsticks))  # Output: True