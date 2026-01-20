from typing import List

def optimalDivision(nums: List[int]) -> str:
    if not nums:
        return ""
    if len(nums) == 1:
        return str(nums[0])
    if len(nums) == 2:
        return f"{nums[0]}/{nums[1]}"
    
    # For 3 or more numbers, put all after the first inside parentheses
    middle = "/".join(map(str, nums[1:]))
    return f"{nums[0]}/({middle})"

print(optimalDivision([1000,100,10,2]))  # "1000/(100/10/2)"
print(optimalDivision([2,3,4]))          # "2/(3/4)"
print(optimalDivision([5000,50,5,2,1]))  # "5000/(50/5/2/1)"
print(optimalDivision([100,10,2,5,2]))   # "100/(10/2/5/2)"