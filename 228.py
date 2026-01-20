from collections import Counter

def topKFrequent(words, k):
    # Step 1: frequency map
    freq = Counter(words)

    # Step 2: sort by (-count, word)
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))

    # Step 3: take top k
    return sorted_words[:k]









from collections import Counter
import heapq

def topKFrequent(words, k):
    # Step 1: frequency map
    freq = Counter(words)

    # Step 2: build a heap of size k
    heap = []
    for word, count in freq.items():
        heapq.heappush(heap, (-count, word))  # negative count for max-heap behavior

    # Step 3: extract k elements
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    
    return result