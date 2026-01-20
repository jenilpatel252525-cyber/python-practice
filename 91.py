def partition(s):
    res = []
    path = []

    def is_palindrome(s, l, r):
        return s[l:r+1] == s[l:r+1][::-1]

    def dfs(start):
        if start == len(s):
            res.append(path[:])
            return

        for end in range(start, len(s)):
            if is_palindrome(s, start, end):
                path.append(s[start:end+1])  # 🎲 choose
                dfs(end + 1)                 # 🧠 explore
                path.pop()                   # ⏪ backtrack

    dfs(0)
    return res