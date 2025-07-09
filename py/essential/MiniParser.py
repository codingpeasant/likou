# https://leetcode.com/problems/mini-parser/description/


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        integerStr = ""

        for c in s:
            if c == "[":
                stack.append(NestedInteger())
            elif c == "]":
                if len(integerStr) > 0:
                    stack[-1].add(NestedInteger(int(integerStr)))
                integerStr = ""
                poppedList = stack.pop()
                if len(stack) == 0:
                    return poppedList
                stack[-1].add(poppedList)
            elif c == ",":
                if len(integerStr) > 0:
                    stack[-1].add(NestedInteger(int(integerStr)))
                integerStr = ""
            else:
                integerStr += c

        return NestedInteger(int(s))
