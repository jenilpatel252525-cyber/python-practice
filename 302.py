from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        freq = Counter(words)

        # arr holds at most k items, each item is a tuple: (-frequency, word)
        arr = []

        def bisect_left_manual(a, key):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                # if a[mid] < key, insertion point is right of mid
                if a[mid] < key:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for word, f in freq.items():
            key = (-f, word)
            idx = bisect_left_manual(arr, key)

            # If insertion index is within top-k (idx < k), insert it.
            # If arr currently has fewer than k items, we also append/insert.
            if idx < k:
                arr.insert(idx, key)
                if len(arr) > k:
                    arr.pop()   # drop lowest-priority item
            else:
                # idx >= k: only append if we still have space (len < k)
                if len(arr) < k:
                    arr.append(key)

        return [w for _, w in arr]












from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):
        # 1. Count frequencies
        freq = Counter(words)

        # 2. Build a heap of (-frequency, word)
        #    Negative frequency makes the heap behave like a max-heap by freq.
        heap = [(-f, w) for w, f in freq.items()]
        heapq.heapify(heap)  # O(m) time to heapify m unique words

        # 3. Pop k times to get the top k words in correct order
        res = []
        for _ in range(k):
            fneg, w = heapq.heappop(heap)
            res.append(w)

        return res





from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):
        freq = Counter(words)  # O(n)

        # Use a min-heap of size at most k. We push (freq, negative-lexicographic) trick
        # but we need ordering: higher freq first, and for tie: lexicographically smaller first.
        # For min-heap we use (freq, word) but with freq positive and we ensure we pop the
        # lowest-priority item when size > k. To get correct final order, we will sort.
        heap = []

        for word, f in freq.items():
            # we want to keep highest freq + lexicographically smallest words.
            # In the min-heap we store (f, -word_order) won't work with strings,
            # so store (f, word) but maintain heap of size k and evict smallest priority.
            heapq.heappush(heap, (f, word))
            if len(heap) > k:
                # pop lowest priority (lowest freq; if tie, lexicographically largest word
                # will be considered larger because of tuple ordering; this keeps correct top-k)
                heapq.heappop(heap)

        # Now heap contains k best in min-heap order (smallest among the best at top).
        # We need final ordering: highest freq first, lexicographically smallest on tie.
        res = sorted(heap, key=lambda x: (-x[0], x[1]))
        return [word for _, word in res]
