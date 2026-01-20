s="abcdefg"

indices=[0,2,4,6]

sources=["abc","cd","e","g"]

targets=["hijk","lmn","opqr","stu"]


class Solution:
    def findReplaceString(self, s, indices, sources, targets):
        ops = sorted(zip(indices, sources, targets))
        res = []
        i = 0

        for idx, src, tgt in ops:
            # add unchanged part
            while i < idx:
                res.append(s[i])
                i += 1
            
            # check if source matches
            if s[idx:idx+len(src)] == src:
                res.append(tgt)
                i = idx + len(src)
        
        # add remaining characters
        res.append(s[i:])
        return "".join(res)