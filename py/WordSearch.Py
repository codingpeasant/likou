# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m, n = len(board), len(board[0])

        def dfs(wordLeft: str, i: int, j: int) -> bool:
            if not wordLeft:
                return True
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or wordLeft[0] != board[i][j]:
                return False

            temp = board[i][j]
            board[i][j] = "."
            found = any(dfs(wordLeft[1:], i + dir[0], j + dir[1]) for dir in dirs)
            board[i][j] = temp
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
