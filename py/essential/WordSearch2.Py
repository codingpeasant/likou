# https://leetcode.com/problems/word-search-ii/
# Trie,DFS,Back Tracking
# Blind
# Neet

from collections import defaultdict
from functools import lru_cache


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word):
        node = self
        for w in word:
            node = node.children[
                w
            ]  # if already exist, use it; else defaultdict creates TrieNode for you as the value
        node.isWord = True

    def search(self, word):
        node = self
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution:
    def findWords(self, board, words):
        res = []
        m, n = len(board), len(board[0])
        trie = Trie()

        for w in words:
            trie.insert(w)

        def dfs(row: int, col: int, node: Trie, path: str):
            # match words starting from node of the trie, board starting from (row, col)
            if node.isWord:
                res.append(path)
                # set to False so not to repeat the same word
                node.isWord = False

            m, n = len(board), len(board[0])
            # similar to two pointers: here is to check if pointer for board reaches its end, or not a match
            if (
                row < 0
                or row >= m
                or col < 0
                or col >= n
                or board[row][col] not in node.children
            ):
                return

            # This is similar to 2 pointers: now a match is found, move the pointer for trie and pointer for board
            tmp = board[row][col]
            board[row][col] = "#"
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in dirs:
                r, c = row + d[0], col + d[1]
                dfs(r, c, node.children[tmp], path + tmp)
            board[row][col] = tmp

        for i in range(m):
            for j in range(n):
                path = ""
                dfs(i, j, trie, path)
        return res


s = Solution()
board = [
    ["a", "b", "c", "e"],
    ["z", "z", "d", "z"],
    ["z", "z", "c", "z"],
    ["z", "a", "b", "z"],
]

words = ["abcdce"]
print(s.findWords(board, words))
