import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]  # Save a copy of the original array
        self.array = nums[:]     # Working copy to shuffle

    def reset(self) -> List[int]:
        self.array = self.original[:]  # Restore from the original
        return self.array

    def shuffle(self) -> List[int]:
        # Fisher-Yates shuffle
        for i in range(len(self.array) - 1, 0, -1):
            j = random.randint(0, i)  # Pick a random index from 0 to i
            self.array[i], self.array[j] = self.array[j], self.array[i]  # Swap
        return self.array[:]
