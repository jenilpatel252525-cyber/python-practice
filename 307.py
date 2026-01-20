s = "aaabbbbccddeee"

import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)

        # ❌ Feasibility check
        if max(freq.values()) > (n + 1) // 2:
            return ""

        # Max heap (use negative counts)
        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap)

        result = []

        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)

            # Append two most frequent characters
            result.append(ch1)
            result.append(ch2)

            # Decrease their counts
            cnt1 += 1   # because cnt is negative
            cnt2 += 1

            if cnt1 < 0:
                heapq.heappush(heap, (cnt1, ch1))
            if cnt2 < 0:
                heapq.heappush(heap, (cnt2, ch2))

        # If one character remains
        if heap:
            result.append(heap[0][1])

        return "".join(result)
