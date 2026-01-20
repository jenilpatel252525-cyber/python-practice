dictionary = ["cat","bat","rat"]

sentence = "the cattle was rattled by the battery"

array=sentence.split(" ")

dictionary.sort(key=len)

for word in dictionary:
    for i in range(len(array)):
        if word in array[i][:len(word)]:
            array[i]=word

print(" ".join(array))





class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False  # Marks the end of a root

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def search_root(self, word):
        node = self.root
        prefix = ""
        for ch in word:
            if ch not in node.children:
                return None  # no root matches
            node = node.children[ch]
            prefix += ch
            if node.is_end:
                return prefix  # return the shortest matching root
        return None

def replaceWords(dictionary, sentence):
    trie = Trie()
    # Insert all roots into Trie
    for root in dictionary:
        trie.insert(root)
    
    words = sentence.split()
    
    # Replace words with shortest root if available
    for i in range(len(words)):
        root = trie.search_root(words[i])
        if root:
            words[i] = root
    
    return " ".join(words)

# Example usage
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

print(replaceWords(dictionary, sentence))