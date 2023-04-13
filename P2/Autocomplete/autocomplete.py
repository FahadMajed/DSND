class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def suffixes(self, suffix=''):
        suffixes = []
        if self.is_word:
            suffixes.append(suffix)
        for char, node in self.children.items():
            suffixes += node.suffixes(suffix + char)
        return suffixes


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()
        pass

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        node = self.root
        for i in range(len(prefix)):

            char = prefix[i]

            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_word


trie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod",
]

for word in wordList:
    trie.insert(word)


print(trie.find("anth"))
# Flase
print(trie.find("trigger"))
# True
print(trie.root.children['f'].suffixes())
# ['un', 'unction', 'actory']
