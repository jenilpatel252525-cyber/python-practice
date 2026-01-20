class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0   # sum of all values for keys passing through this node


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.key_vals = {}  # to remember existing key values

    def insert(self, key: str, val: int) -> None:
        # Find how much this key's value is changing
        old_val = self.key_vals.get(key, 0)
        delta = val - old_val

        # Update hashmap
        self.key_vals[key] = val

        # Walk through the trie and update scores
        node = self.root
        node.score += delta  # root also represents prefix ""
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.score += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.score
