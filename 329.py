from bisect import bisect_right
from collections import defaultdict

class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]  # [(t1, v1), (t2, v2), ...]

        # Find rightmost timestamp <= given timestamp
        idx = bisect_right(arr, (timestamp, chr(127))) - 1

        if idx >= 0:
            return arr[idx][1]
        return ""
