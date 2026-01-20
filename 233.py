def longestWord(words):
    valid = set([""])  # base case: empty word is valid
    ans = ""

    # sort by length first, then lexicographically
    for w in sorted(words, key=lambda x: (len(x), x)):
        if w[:-1] in valid:   # only valid if prefix already exists
            valid.add(w)
            # update answer
            if len(w) > len(ans):
                ans = w
    return ans
