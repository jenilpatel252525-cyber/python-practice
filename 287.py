s = "abpcplea"

dictionary = ["ale","apple","monkey","plea"]

from typing import List
import bisect

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # build char -> list of positions
        char_map = {}
        for i, ch in enumerate(s):
            char_map.setdefault(ch, []).append(i)

        def can_form(word: str) -> bool:
            prev = -1
            for ch in word:
                if ch not in char_map:
                    return False
                positions = char_map[ch]
                # find smallest index strictly greater than prev
                idx = bisect.bisect_right(positions, prev)
                if idx == len(positions):
                    return False
                prev = positions[idx]
            return True

        best = ""
        for w in dictionary:
            if can_form(w):
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
        return best