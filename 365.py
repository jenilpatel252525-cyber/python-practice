a=4
b=5
c=6

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        
        if a > 0: heapq.heappush(heap, (-a, 'a'))
        if b > 0: heapq.heappush(heap, (-b, 'b'))
        if c > 0: heapq.heappush(heap, (-c, 'c'))
        
        ans = []

        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            
            # If last two are same as ch1, try second best
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch1:
                if not heap:
                    break
                
                cnt2, ch2 = heapq.heappop(heap)
                ans.append(ch2)
                cnt2 += 1  # since cnt is negative
                
                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))
                
                heapq.heappush(heap, (cnt1, ch1))
            else:
                ans.append(ch1)
                cnt1 += 1
                
                if cnt1 < 0:
                    heapq.heappush(heap, (cnt1, ch1))
        
        return "".join(ans)



















class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []

        # counts and chars packed together
        freq = [[a, 'a'], [b, 'b'], [c, 'c']]
        freq.sort(reverse=True)  # only once

        while True:
            used = False

            for i in range(3):
                count, ch = freq[i]

                if count == 0:
                    continue

                if len(ans) >= 2 and ans[-1] == ans[-2] == ch:
                    continue

                # use this character
                ans.append(ch)
                freq[i][0] -= 1
                used = True

                # restore order with conditional swaps
                if i < 2 and freq[i][0] < freq[i + 1][0]:
                    freq[i], freq[i + 1] = freq[i + 1], freq[i]
                if i < 1 and freq[i + 1][0] < freq[i + 2][0]:
                    freq[i + 1], freq[i + 2] = freq[i + 2], freq[i + 1]

                break

            if not used:
                break

        return "".join(ans)
