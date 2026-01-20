nums = [2,2,2,2,2]
length = len(nums)

def add(a, b):
    return (a + b) % length

def sub(a, b):
    return (a - b + length) % length

for i in range(len(nums)):
    first = i
    curr = i
    flag = False
    if nums[first] > 0:
        count = 0
        while True:
            if nums[curr] < 0:
                break
            curr = add(curr, nums[curr])
            count += 1
            if curr == first and count > 1:   # ✅ changed condition
                print("true")
                flag = True
                break
            if count > length:
                break
        if flag:
            break
    else:
        count = 0
        while True:
            if nums[curr] > 0:
                break
            curr = sub(curr, nums[curr])
            count += 1
            if curr == first and count > 1:   # ✅ changed condition
                print("true")
                flag = True
                break
            if count > length:
                break
        if flag:
            break

        
        
        
nums = [2, 2, 2, 2, 2]
length = len(nums)

def add(a, b):
    return (a + b) % length

def sub(a, b):
    return (a - b + length) % length

for i in range(length):
    if nums[i] == 0:
        continue

    first = i
    curr = i
    direction = nums[i] > 0
    count = 0

    while True:
        if nums[curr] == 0:
            break
        if (nums[curr] > 0) != direction:
            break

        next_curr = add(curr, nums[curr]) if direction else sub(curr, nums[curr])

        # If it's a valid loop (not self-loop)
        if next_curr == first and count > 0:
            print("true")
            exit()

        # Mark as visited
        temp = curr
        curr = next_curr
        nums[temp] = 0
        count += 1

# If no loop found
print("false")

        
        
        
def circularArrayLoop(nums):
    n = len(nums)

    def next_index(i):
        return (i + nums[i]) % n

    for i in range(n):
        if nums[i] == 0:
            continue

        # Slow and fast pointers
        slow, fast = i, next_index(i)

        # Check same direction and not self-loop
        while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
            if slow == fast:
                # One-element loop is invalid
                if slow == next_index(slow):
                    break
                return True
            slow = next_index(slow)
            fast = next_index(next_index(fast))

        # Mark all visited elements as 0 (to prevent reprocessing)
        val = nums[i]
        j = i
        while nums[j] * val > 0:
            next_j = next_index(j)
            nums[j] = 0
            j = next_j

    return False