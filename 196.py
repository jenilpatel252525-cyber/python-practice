def findLongestWord(s, dictionary):
    
    # def is_subsequence(word):
        # i = j = 0
        # while i < len(s) and j < len(word):
            # if s[i] == word[j]:
                # j += 1
            # i += 1
        # return j == len(word)
    
    def is_subsequence_alt(s, word):
        i = 0  # pointer for s
        for ch in word:
            while i < len(s) and s[i] != ch:
                i += 1
            if i == len(s):  # char not found
                return False
            i += 1  # move to next char in s
        return True

    best = ""
    for word in dictionary:
        if is_subsequence_alt(word):
            if len(word) > len(best) or (len(word) == len(best) and word < best):
                best = word
    return best
