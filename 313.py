s = "(0012300)"

ans = []

# remove parentheses
s = s[1:-1]

def isvalid(s):
    a = s.split(".")
    s1 = a[0]
    s2 = a[1]

    # left part: no leading zero unless single digit
    if len(s1) > 1 and s1[0] == '0':
        return False

    # right part: no trailing zero
    if s2[-1] == '0':
        return False

    return True


def var(s):
    a = []

    # integer without decimal
    if len(s) == 1 or s[0] != '0':
        a.append(s)

    # decimal placements
    for i in range(1, len(s)):
        if isvalid(s[:i] + "." + s[i:]):
            a.append(s[:i] + "." + s[i:])

    return a


def coordinate():
    for i in range(1, len(s)):
        s1 = s[:i]
        s2 = s[i:]

        var1 = var(s1)
        var2 = var(s2)

        for j in var1:
            for k in var2:
                ans.append(f"({j}, {k})")


coordinate()
print(ans)
