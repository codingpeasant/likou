# https://leetcode.com/problems/word-search/
# DFS,Back Tracking
# Blind
# Grind
# Neet

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(wordLeft: str, i: int, j: int) -> bool:
            if not wordLeft:
                return True
            if (
                not 0 <= i < m
                or not 0 <= j < n
                or wordLeft[0] != board[i][j]
                or visited[i][j]
            ):
                return False

            visited[i][j] = True
            found = any(dfs(wordLeft[1:], i + dir[0], j + dir[1]) for dir in dirs)
            visited[i][j] = False
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(word, i, j):
                    return True
        return False


s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(s.exist(board, word))
