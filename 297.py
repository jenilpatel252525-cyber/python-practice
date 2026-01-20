dictionary = ["cat","bat","rat"]

sentence = "the cattle was rattled by the battery"

class Solution:
    def replaceWords(self, dictionary, sentence):
        # 26 buckets
        buckets = [[] for _ in range(26)]
        
        # fill buckets
        for root in dictionary:
            idx = ord(root[0]) - ord('a')
            buckets[idx].append(root)
        
        # sort each bucket so shortest roots appear first
        for b in buckets:
            b.sort(key=len)

        words = sentence.split()
        res = []

        for word in words:
            idx = ord(word[0]) - ord('a')
            replacement = word

            # only check bucket of this starting letter
            for r in buckets[idx]:
                if word.startswith(r):
                    replacement = r
                    break
            
            res.append(replacement)

        return " ".join(res)











class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False  # marks end of a root word


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def get_root_prefix(self, word: str) -> str:
        """
        Return the shortest root that is a prefix of 'word'.
        If none exists, return the original word.
        """
        node = self.root
        prefix_chars = []
        
        for ch in word:
            if ch not in node.children:
                # cannot go further, no matching root
                return word
            node = node.children[ch]
            prefix_chars.append(ch)
            
            if node.is_end:
                # found a root; return it
                return "".join(prefix_chars)
        
        # finished word but didn't hit any root end
        return word


class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        
        # Build the trie with all root words
        for root in dictionary:
            trie.insert(root)
        
        words = sentence.split()
        replaced_words = []
        
        for w in words:
            replaced_words.append(trie.get_root_prefix(w))
        
        return " ".join(replaced_words)
