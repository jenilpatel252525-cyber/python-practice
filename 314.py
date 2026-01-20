class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = True   # assume leaf initially


class Solution:
    def minimumLengthEncoding(self, words):
        # 1. Remove duplicates
        words = list(set(words))

        # 2. Sort by length descending (important)
        words.sort(key=len, reverse=True)

        root = TrieNode()
        nodes = {}  # maps word -> ending node

        # 3. Insert reversed words into trie
        for word in words:
            curr = root
            for ch in reversed(word):
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                    curr.is_leaf = False
                curr = curr.children[ch]
            nodes[word] = curr

        # 4. Count only words that end at leaf nodes
        ans = 0
        for word, node in nodes.items():
            if node.is_leaf:
                ans += len(word) + 1  # +1 for '#'

        return ans
    
    
    
    


class Solution:
    def minimumLengthEncoding(self, words):
        s = set(words)

        for word in words:
            # remove all proper suffixes
            for i in range(1, len(word)):
                s.discard(word[i:])

        # remaining words must be encoded
        return sum(len(word) + 1 for word in s)




class Solution:
    def minimumLengthEncoding(self, words):
        words = list(set(words))
        rev = sorted(w[::-1] for w in words)

        ans = 0
        for i in range(len(rev)):
            # if next word does not start with current
            if i + 1 == len(rev) or not rev[i + 1].startswith(rev[i]):
                ans += len(rev[i]) + 1

        return ans