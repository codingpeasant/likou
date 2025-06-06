# https://leetcode.com/problems/online-stock-span/
# Neet


class StockSpanner:
    def __init__(self):
        self.stack = []  # desc

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        print(self.stack)
        return res


s = StockSpanner()
print(s.next(100))
print(s.next(80))
print(s.next(60))
print(s.next(70))
print(s.next(60))
print(s.next(75))
print(s.next(65))
print(s.next(100))
