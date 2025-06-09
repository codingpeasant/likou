# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# Blind
# Grind
# Neet

from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word: str) -> None:
        node = self
        for letter in word:
            node = node.children[
                letter
            ]  # if already exist, use it; else defaultdict creates Trie for you as the value
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self
        for letter in word:
            node = node.children.get(
                letter
            )  # node.children[letter] will always return an object so cannot be used here
            if not node:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self
        for letter in prefix:
            node = node.children.get(letter)
            if not node:
                return False
        return True


trie = Trie()
trie.insert("abc")
trie.insert("acd")
trie.insert("acc")
print(trie.startsWith("a"))
print(trie.startsWith("c"))
print(trie.search("abc"))
print(trie.search("aqq"))
