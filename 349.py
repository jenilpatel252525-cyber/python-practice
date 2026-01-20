folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

def removeSubfolders(folder):
    folder.sort(key=len)
    parents = set()
    res = []

    for f in folder:
        parts = f.split('/')
        path = ""
        is_sub = False

        for i in range(1, len(parts) - 1):
            path += "/" + parts[i]
            if path in parents:
                is_sub = True
                break

        if not is_sub:
            parents.add(f)
            res.append(f)

    return res










class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_and_check(self, path):
        node = self.root
        parts = path.split("/")[1:]  # skip empty root

        for part in parts:
            if node.is_end:
                return False  # parent folder already exists

            if part not in node.children:
                node.children[part] = TrieNode()

            node = node.children[part]

        node.is_end = True
        return True


def removeSubfolders(folder):
    folder.sort()  # lexicographic sort
    trie = Trie()
    res = []

    for f in folder:
        if trie.insert_and_check(f):
            res.append(f)

    return res
