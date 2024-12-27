# https://leetcode.com/problems/implement-trie-prefix-tree/description/

from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.children[
                letter
            ]  # if already exist, use it; else defaultdict creates TrieNode for you as the value
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            node = node.children.get(
                letter
            )  # node.children[letter] will always return an object so cannot be used here
            if not node:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
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
