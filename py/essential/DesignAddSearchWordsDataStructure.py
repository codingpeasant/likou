# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Neet
# Grind

from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def searchPrefix(self, word: str) -> bool:
        return self.dfs(self.root, word, True)

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, False)

    def dfs(self, node: TrieNode, word: str, is_prefix: bool) -> bool:
        if not word:
            if node.is_word or is_prefix:
                return True
            return False
        if word[0] == ".":
            return any(
                self.dfs(child_node, word[1:], is_prefix)
                for child_node in node.children.values()
            )
        else:
            node = node.children.get(word[0])
            if node:
                return self.dfs(node, word[1:], is_prefix)
            return False


s = WordDictionary()
s.addWord("abc")
s.addWord("abd")
print(s.search(".bc"))
print(s.searchPrefix("a."))
