import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # maps val to its index in list
        self.nums = []          # list to store values

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        # Get index of val to remove
        index_to_remove = self.val_to_index[val]
        last_val = self.nums[-1]

        # Move last element to the place of the one to remove
        self.nums[index_to_remove] = last_val
        self.val_to_index[last_val] = index_to_remove

        # Remove last element
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))   # True
print(randomizedSet.remove(2))   # False
print(randomizedSet.insert(2))   # True
print(randomizedSet.getRandom()) # 1 or 2
print(randomizedSet.remove(1))   # True
print(randomizedSet.insert(2))   # False
print(randomizedSet.getRandom()) # 2