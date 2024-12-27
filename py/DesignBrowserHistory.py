# https://leetcode.com/problems/design-browser-history/description/


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.current += 1
        if self.current == len(self.history):
            self.history.append(url)
        else:
            self.history[self.current] = url
        self.bound = self.current

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.bound, self.current + steps)
        return self.history[self.current]


s = BrowserHistory("0")
s.visit("a")
s.visit("b")
s.visit("c")
s.visit("d")
print(s.back(2))
s.visit("e")
print(s.back(1))
print(s.forward(2))
