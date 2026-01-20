s = "a1b2c"
ans = []

def dfs(i, curr):
    if i == len(s):
        ans.append(curr)
        return

    if s[i].isdigit():
        dfs(i+1, curr + s[i])
    else:
        dfs(i+1, curr + s[i].lower())
        dfs(i+1, curr + s[i].upper())

dfs(0, "")
print(ans)
