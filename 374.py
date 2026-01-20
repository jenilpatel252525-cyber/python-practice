from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        mp = {}
        ans = []

        for name in names:
            if name not in mp:
                ans.append(name)
                mp[name] = 1
            else:
                k = mp[name]
                while f"{name}({k})" in mp:
                    k += 1

                new_name = f"{name}({k})"
                ans.append(new_name)

                mp[name] = k + 1
                mp[new_name] = 1

        return ans
