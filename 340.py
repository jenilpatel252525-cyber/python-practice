board = [
         "abcde", 
         "fghij", 
         "klmno", 
         "pqrst", 
         "uvwxy", 
         "z"
         ]

target = "leet"

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = []
        cr = cc = 0  # current row, col

        for ch in target:
            idx = ord(ch) - ord('a')
            nr = idx // 5
            nc = idx % 5

            # SPECIAL handling for 'z'
            if ch == 'z':
                # move horizontally first
                while cc > nc:
                    res.append('L')
                    cc -= 1
                while cc < nc:
                    res.append('R')
                    cc += 1
                while cr > nr:
                    res.append('U')
                    cr -= 1
                while cr < nr:
                    res.append('D')
                    cr += 1
            else:
                # normal: vertical first
                while cr > nr:
                    res.append('U')
                    cr -= 1
                while cr < nr:
                    res.append('D')
                    cr += 1
                while cc > nc:
                    res.append('L')
                    cc -= 1
                while cc < nc:
                    res.append('R')
                    cc += 1

            res.append('!')

        return "".join(res)
