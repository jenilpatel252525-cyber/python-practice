import heapq

def nthSuperUglyNumber(n, primes):
    ugly = [1]
    heap = []
    
    # Initialize heap with (prime * ugly[0], prime, index)
    for prime in primes:
        heapq.heappush(heap, (prime, prime, 0))
    
    while len(ugly) < n:
        next_ugly, prime, i = heapq.heappop(heap)
        
        # Avoid duplicates
        if next_ugly != ugly[-1]:
            ugly.append(next_ugly)
        
        # Push next candidate from the same prime
        heapq.heappush(heap, (prime * ugly[i+1], prime, i+1))
    
    return ugly[-1]
