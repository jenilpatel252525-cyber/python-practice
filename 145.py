a=[9, 8, 7, 1, 2, 0, 5, 3, 6]

i=0
j=len(a)-1

def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            # num > second > first → triplet found
            return True

    return False