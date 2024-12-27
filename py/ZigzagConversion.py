# https://leetcode.com/problems/zigzag-conversion/
# Simulation


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        listOfList = [[] for y in range(numRows)]

        curRow, diff = 0, 1  # diff 1 downwards, -1 upwards
        for letter in s:
            listOfList[curRow].append(letter)
            if curRow == numRows - 1:
                diff = -1
            elif curRow == 0:
                diff = 1
            curRow += diff

        res = []
        for curList in listOfList:
            res += curList
        return "".join(res)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
