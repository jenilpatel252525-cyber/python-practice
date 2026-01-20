class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str, node=None, i=0) -> bool:
        if node is None:   # first call starts at root
            node = self.root

        if i == len(word):
            return node.isEnd

        ch = word[i]
        if ch == ".":
            for child in node.children.values():
                if self.search(word, child, i + 1):   # ✅ recurse inside search
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self.search(word, node.children[ch], i + 1)